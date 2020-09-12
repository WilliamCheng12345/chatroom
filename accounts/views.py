from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class =UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('home')