import json
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View, FormView
from django.http import HttpResponse
from books.forms import BookForm, GetBookForm, GetStudentForm
from ajax_select.fields import autoselect_fields_check_can_add
from books.models import Books, Borrowship
from students.models import Students


class ViewBooks(FormView):
    FORM_CLASS = GetBookForm

    def get(self, request):

        form = self.FORM_CLASS()

        return render(request, 'index.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.FORM_CLASS()

        book = Books.objects.get(pk=request.POST["title"])

        return render(request, "index.html", {"book": book,
                                              "form": form})


class AddBook(View):

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


class BookView(View):

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
            new_loan = Borrowship(student=Students(pk=student),
                                  book=Books(pk=pk))
            new_loan.save()
            book.amount -= 1
            book.save()
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
