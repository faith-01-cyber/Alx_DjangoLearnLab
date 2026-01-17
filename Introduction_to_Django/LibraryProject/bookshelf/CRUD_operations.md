# CRUD Operations Documentation

## Create
```python
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Retrieve
```python
Book.objects.all()
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
