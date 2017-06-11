# -*- coding: latin-1 -*-

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from books.models import Books, Borrowship
from students.forms import StudentForm
from students.models import Students


class ViewStudents(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "index.html")


class AddStudent(LoginRequiredMixin, View):
    FORM_CLASS = StudentForm

    MODEL = Students

    def get(self, request):
        form = self.FORM_CLASS()

        return render(request, "add_student.html", {"form": form})

    def post(self, request):
        form = self.FORM_CLASS(request.POST)

        if form.is_valid():
            new_student = self.MODEL(**form.cleaned_data)

            new_student.save()

            form = self.FORM_CLASS()

            return render(request, "add_student.html", {"form": form, "message": "Student tillagd"})

        return render(request, "add_student.html", {"form": form})


class StudentView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        students = Students.objects.all().order_by("lastname")

        student = Students.objects.get(pk=pk)
        try:
            loans = Borrowship.objects.filter(student=Students(pk), returned=False)
            books = []
            for loan in loans:
                book = Books.objects.get(pk=loan.book.pk)
                books.append(book)
        except Borrowship.DoesNotExist:
            books = []

        return render(request, "student.html", {"students": students,
                                                "student": student,
                                                "books": books})

    def post(self, request, pk):
        students = Students.objects.all().order_by("lastname")
        student = Students.objects.get(pk=pk)
        book = request.POST.get('book')

        try:
            loan = Borrowship.objects.get(book=Books(book), student=Students(pk), returned=False)
            loan.returned = True
            book = Books.objects.get(pk=book)
            book.amount += 1
            book.save()
            loan.save()
            teacher = loan.user
            send_mail(
                'Skolbiblioteket',
                """Hej {0}:
Hoppas {1} va bra, tack för att du lämnade tillbaka den så andra elever kan läsa den.

Glada hälsningar

Skolbiblioteket""".format(student.firstname, book.title),
                'lilbiblan@skf.com',
                [student.email.replace("\n", ""), teacher.email],
                fail_silently=False,
            )


        except Borrowship.DoesNotExist:
            pass

        try:
            loans = Borrowship.objects.filter(student=Students(pk), returned=False)
            books = []
            for loan in loans:
                book = Books.objects.get(pk=loan.book.pk)
                books.append(book)
        except Borrowship.DoesNotExist:
            books = []

        return render(request, "student.html", {"students": students,
                                             "student": student,
                                             "books": books,})