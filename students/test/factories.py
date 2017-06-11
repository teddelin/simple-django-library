import factory

from students import models


class StudentFactory(factory.DjangoModelFactory):
    """ Factory for the Students model. """
    class Meta:
        model = models.Students

    firstname = 'test'
    lastname = 'testsson'
    email = 'test.testsson@email.com'
