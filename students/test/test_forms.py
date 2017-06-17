from django.test import TestCase

from students.forms import StudentForm
from students.models import Students


class StudentFormTest(TestCase):

    def setUp(self):
        self.entry = Students.objects.create(firstname='test', lastname='testsson', email='test.testsson@email.com')

    def test_init(self):
        StudentForm(self.entry)

    def test_valid_data(self):
        form = StudentForm({
            'firstname': 'Joe',
            'lastname': 'Smith',
            'email': 'joe.smith@email.com'
        })
        self.assertTrue(form.is_valid())

        student = form.save()
        self.assertEqual(student.firstname, 'Joe')
        self.assertEqual(student.lastname, 'Smith')
        self.assertEqual(student.email, 'joe.smith@email.com')
