from django.shortcuts import render
from django.views.generic import DetailView
from .models import Room
# Create your views here.
def renderHomePageView(request):
    return render(request, 'home.html')

def renderChatPageView(request, chatroom_name):
    return render(request, 'chat.html', {
        'chatroom_name': chatroom_name
    })

class RoomsDetailView(DetailView):
    model = Room
    template_name = 'rooms_detail.html'
    slug_url_kwarg = 'chatroom_name'

