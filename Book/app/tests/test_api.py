from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Book
from app.serializers import BookSerializer


class BookApiTestCase(APITestCase):
    def test_get(self):
        book1 = Book.objects.create(name='test book 1', price= 25)
        book2 = Book.objects.create(name= 'test book 2', price= 26)
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([book1, book2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

