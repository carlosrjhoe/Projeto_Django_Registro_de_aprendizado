from django.shortcuts import render

# Create your views here.
def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'users/index.html')