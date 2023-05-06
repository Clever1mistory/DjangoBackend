from django.test import TestCase

from app.models import Book
from app.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book1 = Book.objects.create(name='test book 1', price=25,
                                    author_name='Author 1')
        book2 = Book.objects.create(name='test book 2', price=26,
                                    author_name='Author 2')
        data = BookSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'test book 1',
                'price': '25.00',
                'author_name': 'Author 1'
            },
            {
                'id': book2.id,
                'name': 'test book 2',
                'price': '26.00',
                'author_name': 'Author 2'
            }
        ]
        self.assertEqual(expected_data, data)
