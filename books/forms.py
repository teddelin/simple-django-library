from django import forms
from django.forms import ModelForm
from books.models import Books
from students.models import Students
from ajax_select.fields import AutoCompleteSelectField

class BookForm(ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author', 'category', 'isbn']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(BookForm, self).clean()

        return cleaned_data


class GetBookForm(forms.Form):
    class Meta:
        model = Books

    title = AutoCompleteSelectField('title', required=False, help_text=None)


class GetStudentForm(forms.Form):
    class Meta:
        model = Students

        firstname = AutoCompleteSelectField('firstname', required=False, help_text=None)