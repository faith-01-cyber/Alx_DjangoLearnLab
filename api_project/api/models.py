from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

class Author(models.Model):
    """Represents an author."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a book."""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def clean(self):
        if self.publication_year > datetime.now().year:
            raise ValidationError("Publication year cannot be in the future.")

    def __str__(self):
        return self.title

