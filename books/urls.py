from django.conf.urls import url, include
from ajax_select import urls as ajax_select_urls
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^login/$', views.login_to_app, name='login'),
    url(r'^create_user/$', views.UserCreation.as_view(), name='create_user'),
    url(r'^login_to_app/$', views.login_to_app, name='login_to_app'),
    url(r'^logout/$', views.logout_of_app, name='logout_of_app'),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^find_book/$', views.ViewBooks.as_view(), name='find_book'),
    url(r'^add_book/$', views.AddBook.as_view(), name='add_book'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookView.as_view(), name='view_book'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)