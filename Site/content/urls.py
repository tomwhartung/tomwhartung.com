
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    re_path(r'^(?P<unknown_page>.*)$', views.not_found, name='not_found'),
]
