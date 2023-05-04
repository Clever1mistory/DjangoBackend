from rest_framework.viewsets import ModelViewSet

from app.models import Book
from app.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


