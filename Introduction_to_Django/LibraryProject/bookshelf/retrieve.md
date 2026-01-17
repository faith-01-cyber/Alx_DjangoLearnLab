## Retrieve Book

```python
from bookshelf.models import Book
# Retrieve the book using .get()
book = Book.objects.get(title="1984")
book
```

# Output:
# <Book: 1984>
