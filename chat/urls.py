from django.urls import path
from .views import (
    renderHomePageView,
    renderChatPageView,
    CreateRoomView
)

urlpatterns = [
    path('', renderHomePageView, name='home'),
    path('newRoom/', CreateRoomView.as_view(), name='room_new'),
    path('<str:room_name>/', renderChatPageView, name='chat'),

]