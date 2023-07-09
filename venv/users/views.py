from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
class Login(LoginView):
    """A página inicial de login"""
    redirect_authenticated_user = True

    # def get_success_url(self):
    #     return reverse_lazy('tasks') 
    
    # def form_invalid(self, form):
    #     messages.error(self.request,'Invalid username or password')
    #     return self.render_to_response(self.get_context_data(form=form)) 