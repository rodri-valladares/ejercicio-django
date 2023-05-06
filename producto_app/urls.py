from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ejemplo/', views.ejemplo_template, name='ejemplo'),
]