from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from books.forms import BookForm
from books.models import Books

# Create your views here.
def index(request):
    return HttpResponse("Ursäkta röran vi byggger om")


class ViewBooks(View):

    def get(self, request):
        return render(request, 'index.html')

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
        return render(request, 'add_book.html', {'form': form})