from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:chatroom_name>/', consumers.ChatConsumer),
]