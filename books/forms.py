from django import forms
from dal import autocomplete
from django.forms import ModelForm
from books.models import Books
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

class BookForm(ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author', 'category', 'iban']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(BookForm, self).clean()

        return cleaned_data


class GetBookForm(forms.Form):
    class Meta:
        model = Books

    title = AutoCompleteSelectField('title', required=False, help_text=None)