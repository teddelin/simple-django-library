from django import forms
from django.forms import ModelForm
from students.models import Students
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ["firstname", "lastname", "email"]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        return cleaned_data
