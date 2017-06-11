from django.test import TestCase

from books.forms import BookForm
from books.models import Books


class BookFormTest(TestCase):

    def setUp(self):
        self.entry = Books.objects.create(title='testing',
                                          author='test testsson',
                                          category='Unit testing')

    def test_init(self):
        BookForm(self.entry)

    def test_valid_data(self):
        form = BookForm({
            'title': 'Unit testing 123',
            'author': 'test testsson',
            'category': 'Unit testing'
        })
        self.assertTrue(form.is_valid())

        book = form.save()
        self.assertEqual(book.title, 'Unit testing 123')
        self.assertEqual(book.author, 'test testsson')
        self.assertEqual(book.category, 'Unit testing')
        self.assertEqual(book.amount, 1)
