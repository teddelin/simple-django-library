from django import forms
from django.forms import ModelForm
from books.models import Books

class BookForm(ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author', 'category', 'iban']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(BookForm, self).clean()

        return cleaned_data