from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ViewBooks.as_view(), name='index'),
    url(r'^add_book/$', views.AddBook.as_view(), name='add_book'),
]