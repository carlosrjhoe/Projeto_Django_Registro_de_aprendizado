from django.urls import path
from .views import Login

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(template_name='users/login.html'), name='login'),
]