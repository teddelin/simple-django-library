from django.contrib.auth.models import User
import factory

from books import models
from students.test import factories


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%d" % n)


class BookFactory(factory.DjangoModelFactory):
    """ Factory for the Books model. """
    class Meta:
        model = models.Books

    title = 'testing python'
    author = 'test testsson'
    category = 'Unit testing'
    isbn = '9780747532743'
    amount = 1


class BorrowshipFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Borrowship

    book = factory.SubFactory(BookFactory)
    student = factory.SubFactory(factories.StudentFactory)
    user = factory.SubFactory(UserFactory)
