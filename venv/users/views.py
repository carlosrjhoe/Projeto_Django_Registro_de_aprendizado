from django.shortcuts import render

# Create your views here.
def login(request):
    """A página inicial de login"""
    return render(request, 'users/login.html')