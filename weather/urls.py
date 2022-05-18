from unicodedata import name

from django import views
from django.contrib import admin
from django.urls import path,include
from weather import views

urlpatterns = [
    path('',views.index, name='home'),
    path('delete/<city_name>/',views.delete, name='delete'),
]