from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    A form for creating and editing Notes.
    """

    class Meta:
        model = Note

        # Which fields to include in the form
        fields = ['title', 'content']

        # Custom widgets for better styling and usability
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title',
                'required': True,
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note content',
                'rows': 5,
                'required': True,
            }),
        }

        # Custom labels for the fields
        labels = {
            'title': 'Title',
            'content': 'Content',
        }

        # Help text that appears below each field
        help_texts = {
            'title': 'The title of your note (max 200 characters).',
            'content': 'Write your note content here.',
        }
