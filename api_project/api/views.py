from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


class BookList(List.APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

