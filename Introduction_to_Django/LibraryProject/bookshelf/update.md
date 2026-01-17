## Update Book

```python
from bookshelf.models import Book
# Retrieve the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
```

# Output:
# <Book: Nineteen Eighty-Four>
