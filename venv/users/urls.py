from django.urls import path
from . import views
from django.contrib.auth import login

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
]