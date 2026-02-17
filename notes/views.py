from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display a list of all sticky notes.

    URL: /notes/
    Template: notes/note_list.html
    """
    # Get all notes from the database
    notes = Note.objects.all()

    # Render the template with the notes data
    return render(request, 'notes/note_list.html', {
        'notes': notes
    })


def note_detail(request, pk):
    """
    Display a single note's details.

    pk = primary key = the note's ID number

    URL: /notes/<pk>/
    TemplateL: notes/note_detail.html
    """
    # Get ONE specific note by its ID
    note = get_object_or_404(Note, pk=pk)

    return render(request, 'notes/note_detail.html', {
        'note': note
    })


def note_create(request):
    """
    Create a new sticky note.

    Handles both the GET and POST request.

    URL: /notes/new/
    Template: notes/note_form.html
    """
    if request.method == 'POST':
        # If the form was submitted, create a form instance with the data
        form = NoteForm(request.POST)

        if form.is_valid():
            # Save the new note to the database
            note = form.save()

            # Show a success message
            messages.success(request, 'Note created successfully!')

            # Redirect to the new note's detail page
            return redirect('note_detail', pk=note.pk)
    else:
        # User just wants to see the form (GET request)
        form = NoteForm()

    return render(request, 'notes/note_form.html', {
        'form': form,
        'action': 'Create',
    })


def note_update(request, pk):
    """
    Update an existing sticky note.

    URL: /notes/<pk>/edit/
    Template: notes/note_form.html
    """
    # Get the existing note
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        # Create a form instance with the submitted data and the existing note
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            # Save the updated note to the database
            note = form.save()

            # Show a success message
            messages.success(request, 'Note updated successfully!')

            # Redirect to the note's detail page
            return redirect('note_detail', pk=note.pk)
    else:
        # User wants to see the form with the current note data (GET request)
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {
        'form': form,
        'action': 'Update',
        'note': note,
    })


def note_delete(request, pk):
    """
    Delete a sticky note.

    URL: /notes/<pk>/delete/
    Template: notes/note_confirm_delete.html
    """
    # Get the note to delete
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        # User confirmed deletion, so delete the note
        note.delete()

        # Show a success message
        messages.success(request, 'Note deleted successfully!')

        # Redirect to the note list
        return redirect('note_list')

    return render(request, 'notes/note_confirm_delete.html', {
        'note': note
    })
