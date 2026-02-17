from django.db import models


class Note(models.Model):
    """
    A sticky note with a title and content.

    Attributes:
        title: The note's title (max 200 characters)
        content: The note's content (unlimited length)
        created_at: When the note was created (automatic)
        updated_at: When the note was last updated (automatic)
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        """
        Provides extra options for the model.
        """
        # Order notes by newest first
        ordering = ['-created_at']

        # Human-readable names
        verbose_name = 'Sticky Note'
        verbose_name_plural = 'Sticky Notes'
