from django.contrib.auth.models import User
from django.test import TestCase

from books.forms import BookForm, GetBookForm, LoginForm
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


class GetBookFormTest(TestCase):

    def setUp(self):
        self.entry = Books.objects.create(title='testing',
                                          author='test testsson',
                                          category='Unit testing')

    def test_valid_data(self):
        form = GetBookForm({
            'title': 1
        })
        self.assertTrue(form.is_valid())


class LoginFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                             email='test.testsson@email.com',
                                             password='test123')

    def tearDown(self):
        self.user.delete()

    def test_valid_data(self):
        form = LoginForm({
            'username': 'test',
            'password': 'test123'
        })
        self.assertTrue(form.is_valid())
