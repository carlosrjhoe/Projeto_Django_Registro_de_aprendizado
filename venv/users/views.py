from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def login(request):
    """Faz login do usuário."""
    return render(request, 'users/login.html')

def logout_view(request):
    """Faz logout do usuário."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))