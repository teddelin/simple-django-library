import json
from django.shortcuts import render
from django.views.generic import View, FormView
from django.http import HttpResponse
from books.forms import BookForm, GetBookForm
from books.models import Books


class ViewBooks(FormView):
    FORM_CLASS = GetBookForm
    MODEL = Books

    def get(self, request):

        form = self.FORM_CLASS()

        return render(request, 'index.html', {'form': form})


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