from django.contrib import admin
from django.urls import path, include

from base import views

urlpatterns = [
    path('index', views.index),
    path('new', views.new_page),
    path('servey', views.servey),
    path('calculate', views.calculate),
    path('register', views.register),

]
