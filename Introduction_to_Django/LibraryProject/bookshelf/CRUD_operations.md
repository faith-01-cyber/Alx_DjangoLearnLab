# CRUD Operations Documentation

## Create
```python
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Retrieve
```python
book = Book.objects.get(title="1984")
```

## Update
```python
book.title = "Nineteen Eighty-Four"
book.save()
```

## Delete
```python
book.delete()
```
