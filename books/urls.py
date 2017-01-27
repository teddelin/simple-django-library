from django.conf.urls import url, include
from ajax_select import urls as ajax_select_urls
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^find_book/$', views.ViewBooks.as_view(), name='find_book'),
    url(r'^add_book/$', views.AddBook.as_view(), name='add_book'),
   # url(r'^find_book/(?P<pk>[0-9]+)$', views.ViewBooks.as_view(), name='view_book'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)