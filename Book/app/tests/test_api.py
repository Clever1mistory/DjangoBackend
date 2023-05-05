from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Book
from app.serializers import BookSerializer


class BookApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.book1 = Book.objects.create(name='test book 1', price=25,
                                         author_name='Author 1')
        self.book2 = Book.objects.create(name='test book 2', price=26,
                                         author_name='Author 5')
        self.book3 = Book.objects.create(name='test book Author 1', price=26,
                                         author_name='Author 3')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book1, self.book2,
                                          self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book1, self.book2,
                                          self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BookSerializer([self.book1,
                                          self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_order(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'name'})
        serializer_data = BookSerializer([self.book1, self.book2,
                                          self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
