from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Book, Library


# Function-based view: list all books
from django.http import HttpResponse

def list_books(request):
    books = Book.objects.all()
    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")
    return HttpResponse("\n".join(output))


# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

