from django.test import TestCase

from app.models import Book
from app.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book1 = Book.objects.create(name='test book 1', price=25)
        book2 = Book.objects.create(name='test book 2', price=26)
        data = BookSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'test book 1',
                'price': '25.00'
            },
            {
                'id': book2.id,
                'name': 'test book 2',
                'price': '26.00'
            }
        ]
        self.assertEqual(expected_data, data)
