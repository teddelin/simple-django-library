from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory

from students.views import ViewStudents, AddStudent, StudentView
from students.models import Students


class ViewStudentsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_view_call(self):
        request = self.factory.get('/students/')
        response = ViewStudents().get(request)
        self.assertEqual(response.status_code, 200)


class AddStudentTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_view_get_call(self):
        request = self.factory.get('/students/add_student/')
        response = AddStudent().get(request)
        self.assertEqual(response.status_code, 200)

    def test_view_post_call(self):
        amount_before = len(Students.objects.all())
        request = self.factory.post('/students/add_student/',
                                    {
                                        'firstname': 'test',
                                        'lastname': 'testsson',
                                        'email': 'test.testsson@gmail.com'
                                    })
        response = AddStudent().post(request)
        self.assertEqual(response.status_code, 200)
        amount_after = len(Students.objects.all())
        self.assertGreater(amount_after, amount_before)

    def test_view_post_invalid_call(self):
        request = self.factory.post('/students/add_student/',
                                    {
                                        'first_name': 'test',
                                        'lastname': 'testsson',
                                        'email': 'test.testsson@gmail.com'
                                    })
        response = AddStudent().post(request)
        self.assertEqual(response.status_code, 200)


class StudentViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.student = Students.objects.create(firstname='test', lastname='testsson', email='test.testsson@email.com')

    def test_view_get_call(self):
        request = self.factory.get('/students/student/1')
        response = StudentView().get(request, 1)
        print(response)
        self.assertEqual(response.status_code, 200)
