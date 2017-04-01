# -*- coding: latin-1 -*-
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

from books.models import Books, Borrowship
from students.models import Students

def send_reminder():
    high_date = datetime.today() - timedelta(days=29)
    low_date = datetime.today() - timedelta(days=28)
    four_week_notifications = Borrowship.objects.filter(returned=False).filter(date__range=[low_date, high_date])

    for loan in four_week_notifications:

        student = Students.objects.get(pk=loan.student.pk)
        book = Books.objects.get(pk=loan.book.pk)
        send_mail(
            'Skolbiblioteket',
            """Hej {0}:

Du har nu lånat  {1} under 4 veckors tid. Hoppas du hunnit läsa ut boken för nu är det dags att lämna tillbaka den.

Om den inte lämnas tillbaka till utlånande lärare för avregistrering inom en vecka kommer vi att debitera dig 75% av bokens inköpspris.

Skolbiblioteket """.format(student.firstname, book.title),
            'lilbiblan@skf.com',
            [student.email.replace("\n", ""), ],
            fail_silently=False,
        )
    high_date = datetime.today() - timedelta(days=22)
    low_date = datetime.today() - timedelta(days=21)
    three_week_notifications = Borrowship.objects.filter(returned=False).filter(date__range=[low_date, high_date])
    for loan in three_week_notifications:
        student = Students.objects.get(pk=loan.student.pk)
        book = Books.objects.get(pk=loan.book.pk)
        send_mail(
            'Skolbiblioteket',
            """Hej {0}:
Vi hoppas att du tycker {1} är bra.
Detta är en påminnelse om att läsa ut den så att du kan lämna tillbaka den om en vecka.


Glada hälsningar

Skolbiblioteket """.format(student.firstname, book.title),
            'lilbiblan@skf.com',
            [student.email.replace("\n", ""), ],
            fail_silently=False,
        )

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        send_reminder()
