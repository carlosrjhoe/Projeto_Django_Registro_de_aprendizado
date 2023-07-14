from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', views.login, name='login'),
    # Página de logout
    path('logout/', views.logout_view, name='logout'),
    # Página de registro
    path('register/', views.register, name='register'),
]