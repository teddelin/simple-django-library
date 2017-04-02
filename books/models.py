from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from students.models import Students


class Books(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Borrowship(models.Model):

    book = models.ForeignKey(Books)
    student = models.ForeignKey(Students)
    user = models.ForeignKey(User)

    date = models.DateField(default=timezone.now)
    returned = models.BooleanField(default=False)

