from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ViewStudents.as_view(), name="index"),
    url(r'^add_student/$', views.AddStudent.as_view(), name="add_student"),
]