from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from students.forms import StudentForm
from students.models import Students


def index(request):
    return HttpResponse("Vad fan du vill typ")

class ViewStudents(View):
    def get(self, request):
        return render(request, "index.html")

class AddStudent(View):
    FORM_CLASS = StudentForm

    MODEL = Students

    def get(self, request):
        form = self.FORM_CLASS()

        return render(request, "add_student.html", {"form": form})

    def post(self, request):
        form = self.FORM_CLASS(request.POST)

        if form.is_valid():
            new_student = self.MODEL(**form.cleaned_data)

            new_student.save()

        form = self.FORM_CLASS()

        return render(request, "add_student.html", {"form": form})