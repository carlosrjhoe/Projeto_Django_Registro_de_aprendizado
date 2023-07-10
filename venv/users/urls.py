from django.urls import path
from . import views
from django.contrib.auth import login, logout

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]