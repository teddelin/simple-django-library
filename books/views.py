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

    def get(self, request, pk, *args, **kwargs):

        book = Books.objects.get(pk=pk)

        return render(request, "book.html", {"book": book})
