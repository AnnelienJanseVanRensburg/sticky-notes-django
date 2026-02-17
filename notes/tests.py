from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm
import time


class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note Title",
            content="This is the content of the test note. It can be long!"
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note Title")
        self.assertEqual(
            self.note.content,
            "This is the content of the test note. It can be long!"
        )
        # Verify the note was saved to the database
        self.assertEqual(Note.objects.count(), 1)

    def test_note_string_representation(self):
        self.assertEqual(str(self.note), "Test Note Title")

    def test_note_has_timestamps(self):
        self.assertIsNotNone(self.note.created_at)
        self.assertIsNotNone(self.note.updated_at)

    def test_note_ordering(self):
        """
        Test that notes are ordered by creation date (newest first)
        """
        # Create additional notes
        Note.objects.create(
            title="Second Note",
            content="Second not content."
        )
        Note.objects.create(
            title="Third Note",
            content="Third note content."
        )

        # Get all notes
        notes = Note.objects.all()
        self.assertEqual(notes[0].title, "Third Note")
        self.assertEqual(notes[1].title, "Second Note")
        self.assertEqual(notes[2].title, "Test Note Title")

    def test_note_timestamps_update_correctly(self):
        original_updated_at = self.note.updated_at

        # Wait a tiny bit to ensure time passes
        time.sleep(0.01)

        # Modify and save the note
        self.note.title = "Modified Title"
        self.note.save()

        # Refresh from database
        self.note.refresh_from_db()

        # updated_at should be different now, created_at should stay the same
        self.assertNotEqual(self.note.updated_at, original_updated_at)


class NoteFormTest(TestCase):
    def test_note_form_valid_data(self):
        form_data = {
            "title": "Valid Note Title",
            "content": "This is valid content for the note."
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_note_form_missing_title(self):
        form_data = {
            "title": "",  # Empty title should be invalid
            "content": "Content without a title"
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_note_form_missing_content(self):
        form_data = {
            "title": "Title without content",
            "content": ""  # Empty content should be invalid
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)

    def test_note_form_has_correct_fields(self):
        form = NoteForm()
        # Should have exactly these fields
        self.assertEqual(list(form.fields.keys()), ["title", "content"])


class NoteListViewTest(TestCase):
    def setUp(self):
        # Create multiple test notes
        self.note1 = Note.objects.create(
            title="First Note",
            content="First note content"
        )
        self.note2 = Note.objects.create(
            title="Second Note",
            content="Second note content"
        )

    def test_note_list_view_url_exists(self):
        response = self.client.get("/notes/")
        self.assertEqual(response.status_code, 200)

    def test_note_list_view_url_by_name(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)

    def test_note_list_view_uses_correct_template(self):
        response = self.client.get(reverse("note_list"))
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_list_view_displays_all_notes(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        # Check that both notes appear in the response
        self.assertContains(response, "First Note")
        self.assertContains(response, "Second Note")

    def test_note_list_view_shows_empty_message(self):
        # Delete all notes
        Note.objects.all().delete()
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)

        # Should contain the empty state message
        self.assertContains(response, "No notes yet!")
        self.assertContains(response, "Create your first sticky note")


class NoteDetailViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Detail Test Note",
            content="The detailed content of the test note."
        )

    def test_note_detail_view_url_exists(self):
        response = self.client.get(f"/notes/{self.note.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_note_detail_view_url_by_name(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_view_uses_correct_template(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertTemplateUsed(response, "notes/note_detail.html")

    def test_note_detail_view_displays_correct_note(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Detail Test Note")
        self.assertContains(response, "The detailed content of the test note.")

    def test_note_detail_view_404_for_invalid_id(self):
        response = self.client.get(reverse("note_detail", args=[99999]))
        self.assertEqual(response.status_code, 404)


class NoteCreateViewTest(TestCase):
    def test_note_create_view_get(self):
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        # Should contain an empty form
        self.assertIsInstance(response.context["form"], NoteForm)

    def test_note_create_view_post_valid_data(self):
        form_data = {
            "title": "Newly Created Note",
            "content": "This note was created via POST request."
        }
        response = self.client.post(reverse("note_create"), data=form_data)

        # Should redirect after successful creation
        self.assertEqual(response.status_code, 302)

        # Verify the note was created in the database
        self.assertEqual(Note.objects.count(), 1)
        new_note = Note.objects.first()
        self.assertEqual(new_note.title, "Newly Created Note")
        self.assertEqual(
            new_note.content, "This note was created via POST request."
        )

    def test_note_create_view_post_invalid_data(self):
        form_data = {
            "title": "",  # Invalid: empty title
            "content": "Content without title"
        }
        response = self.client.post(reverse("note_create"), data=form_data)

        # Should not redirect, should show form again with errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")

        # No note should be created
        self.assertEqual(Note.objects.count(), 0)


class NoteUpdateViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Original Title",
            content="Original content"
        )

    def test_note_update_view_get(self):
        response = self.client.get(reverse("note_update", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        # Form should be pre-filled with existing note data
        form = response.context["form"]
        self.assertEqual(form.instance, self.note)

    def test_note_update_view_post_valid_data(self):
        form_data = {
            "title": "Updated Title",
            "content": "Updated content"
        }
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            data=form_data
        )

        # Should redirect after successful update
        self.assertEqual(response.status_code, 302)

        # Refresh the note from database and verify changes
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated content")

    def test_note_update_view_post_invalid_data(self):
        form_data = {
            "title": "",  # Invalid: empty title
            "content": "Some content"
        }
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            data=form_data
        )

        # Should not redirect
        self.assertEqual(response.status_code, 200)

        # Note should not be updated
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Original Title")


class NoteDeleteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Note to Delete",
            content="This note will be deleted"
        )

    def test_note_delete_view_get(self):
        response = self.client.get(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")
        self.assertContains(response, "Note to Delete")

    def test_note_delete_view_post(self):
        response = self.client.post(reverse(
            "note_delete", args=[self.note.pk]
        ))
        # Should redirect after deletion
        self.assertEqual(response.status_code, 302)

        # Note should be deleted from database
        self.assertEqual(Note.objects.count(), 0)

        # Verify the specific note no longer exists
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(pk=self.note.pk)
