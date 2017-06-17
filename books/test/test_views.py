from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory

from books.test.factories import BorrowshipFactory
from students.views import ViewStudents, AddStudent, StudentView
from students.models import Students


class ViewBooksTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_view_call(self):
        request = self.factory.get('/')
        response = ViewStudents().get(request)
        self.assertEqual(response.status_code, 200)