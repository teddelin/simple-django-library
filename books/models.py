from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.title
