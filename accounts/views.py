from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from chat.models import Room
# Create your views here.

class SignUpView(CreateView):
    form_class =UserCreationForm
    template_name = 'sign-up.html'
    success_url = reverse_lazy('home')

def renderAccountView(request):
    if request.user.is_authenticated:
        logged_in_user_rooms = Room.objects.filter(creator=request.user)
        return render(request, 'account.html', {'rooms': logged_in_user_rooms})
    else:
        raise PermissionDenied