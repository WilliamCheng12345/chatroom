from django.urls import path
from .views import (
    renderHomePageView,
    renderChatPageView,
    RoomsDetailView,
)

urlpatterns = [
    path('<str:chatroom_name>/', renderChatPageView, name='chat'),
    path('<slug:chatroom_name/chatHistory/', RoomsDetailView.as_view(), name='rooms_detail'),
    path('', renderHomePageView, name='home'),
]