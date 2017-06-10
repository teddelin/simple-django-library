from ajax_select.fields import AutoCompleteSelectField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import Form, ModelForm, ValidationError

from books.models import Books
from students.models import Students

class BookForm(ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author', 'category', 'isbn', 'amount']

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

class LoginForm(Form):
    """
    Manage logins to the app.
    """
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        """
        Make sure the login worked.

        :return: dict, the cleaned_data.
        """
        user = self.login()

        if not user or not user.is_active:
            raise ValidationError('Sorry that was an invalid login. Please try again.')

        return self.cleaned_data

    def login(self):
        """
        Authenticate the user for logging in.

        :return: User, the authenticated user.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        return user


class UserForm(ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
