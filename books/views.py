# -*- coding: latin-1 -*-

import json

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect, Http404
from django.contrib import messages
from django.views.generic import View, FormView
from django.core.mail import send_mail
from django.http import HttpResponse
from books.forms import BookForm, GetBookForm, GetStudentForm, LoginForm, UserForm
from ajax_select.fields import autoselect_fields_check_can_add
from books.models import Books, Borrowship
from students.models import Students


class ViewBooks(LoginRequiredMixin, FormView):
    FORM_CLASS = GetBookForm

    def get(self, request):

        form = self.FORM_CLASS()

        return render(request, 'index.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.FORM_CLASS()

        book = Books.objects.get(pk=request.POST["title"])

        return render(request, "index.html", {"book": book,
                                              "form": form})


class AddBook(LoginRequiredMixin, View):

    FORM_CLASS = BookForm
    MODEL = Books

    def get(self, request):

        form = self.FORM_CLASS()

        return render(request, 'add_book.html', {'form': form})

    def post(self, request):

        form = self.FORM_CLASS(request.POST)

        if form.is_valid():
            new_book = self.MODEL(**form.cleaned_data)
            new_book.save()
            form = self.FORM_CLASS()

            return render(request, 'add_book.html', {'form': form, 'message': 'Bok tillagd'})

        return render(request, 'add_book.html', {'form': form})


class BookView(LoginRequiredMixin, View):

    FORM_CLASS = GetStudentForm

    def get(self, request, pk, *args, **kwargs):
        students = Students.objects.all().order_by("lastname")
        form = self.FORM_CLASS()

        book = Books.objects.get(pk=pk)
        try:
            loans = Borrowship.objects.filter(book=Books(pk), returned=False)
            borrowers = []
            for loan in loans:
                student = Students.objects.get(pk=loan.student.pk)
                borrowers.append(student.firstname+' '+student.lastname)
        except Borrowship.DoesNotExist:
            borrowers = []

        return render(request, "book.html", {"book": book,
                                             "students": students,
                                             "borrowers": ", ".join(borrowers)})

    def post(self, request, pk):

        students = Students.objects.all().order_by("lastname")
        borrowers = []
        book = Books.objects.get(pk=pk)
        student = request.POST.get('student')

        # Check if there are enough books to borrow
        if book.amount > 0:
            student = Students.objects.get(pk=student)
            book = Books.objects.get(pk=pk)
            new_loan = Borrowship(student=student,
                                  book=book,
                                  user=request.user)
            new_loan.save()
            book.amount -= 1
            book.save()
            teacher = new_loan.user
            send_mail(
                'Skolbiblioteket',
                """Hej {0}:
Du har just nu lånat {1}.
Den skall lämnas tillbaka inom 4 veckor.
Hoppas du tycker boken är bra.

Glada hälsningar

Skolbiblioteket""".format(student.firstname, book.title),
                'lilbiblan@skf.com',
                [student.email.replace("\n", ""), teacher.email],
                fail_silently=False,
            )
        else:
            messages.error(request, 'Alla böcker utlånade')
        try:
            loans = Borrowship.objects.filter(book=Books(pk), returned=False)
            borrowers = []
            for loan in loans:
                student = Students.objects.get(pk=loan.student.pk)
                borrowers.append(student.firstname + ' ' + student.lastname)
        except Borrowship.DoesNotExist:
            borrowers = []

        return render(request, "book.html", {"book": book,
                                             "students": students,
                                             "borrowers": ", ".join(borrowers)})


class UserCreation(LoginRequiredMixin, View):
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)

            return HttpResponseRedirect('/create_user')
        form = UserForm()

        return render(request, 'user_creation.html', {'form': form})

    def get(self, request):
        form = UserForm()
        return render(request, 'user_creation.html', {'form': form})

def login_to_app(request):
    """
    Login is required to access the main pages.

    The login screen passes data through to here where we can validate and then redirect.

    Currently we redirect to the 'Create Session' page.

    :param request: HTTP request object
    :return: redirect to the load_file window.
    """

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.login()

            if user:
                login(request, user)

                if request.POST.get('next'):
                    return redirect(request.POST.get('next', 'find_book'))
                else:
                    return redirect('find_book', )
    else:
        form = LoginForm()
    # If we have reached here, the user has not registered as logged in.
    return render(request, 'login.html', {'form': form})


def logout_of_app(request):
    """
    Basic view to logout a user. Redirects to the login screen.

    :param request: HTTP Request containing the user.
    :return: redirect to login page.
    """
    logout(request)
    return redirect('login')
