from django.conf.urls import url

from students import views


urlpatterns = [
    url(r'^$', views.ViewStudents.as_view(), name="index"),
    url(r'^add_student/$', views.AddStudent.as_view(), name="add_student"),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentView.as_view(), name='view_student'),
]