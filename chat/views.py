from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Room
from .forms import RoomForm
from django.http import HttpResponseRedirect
from  django.urls import reverse, reverse_lazy

# Create your views here.
class CreateRoomView(CreateView):
    model = Room
    template_name = 'room-new.html'
    fields = ['room', 'password']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.slug = form.instance.room
        return super().form_valid(form)

class DeleteRoomView(DeleteView):
    model = Room
    template_name = 'room-delete.html'
    success_url = reverse_lazy('home')
    slug_url_kwarg = 'room_name'
    slug_field = 'slug'

def renderHomePageView(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            room_name = form.cleaned_data['room']
            room_password = form.cleaned_data['password']

            if Room.objects.filter(room=room_name).exists():
                requested_room = Room.objects.get(room=room_name)

                if room_password == requested_room.password:
                    request.session['form-submitted ' + room_name] = True

                    return HttpResponseRedirect(reverse('chat', kwargs={'room_name': room_name}))
                else:
                    return render(request, 'incorrect-password.html')
            else:
                return render(request, 'nonexistent-room.html')
    else:
        form = RoomForm()

    return render(request, 'home.html', {'form': form})

def renderChatPageView(request, room_name):
    if not request.session.get('form-submitted ' + room_name, False):
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'chat.html', {
            'room_name': room_name
        })

