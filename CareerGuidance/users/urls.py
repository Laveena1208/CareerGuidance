from django.urls import path

from .models import Login
from . import views as views

urlpatterns = [
   
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
]