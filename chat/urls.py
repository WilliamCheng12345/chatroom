from django.urls import path
from .views import (
    renderHomePageView,
    renderChatPageView,
    CreateRoomView,
    DeleteRoomView,
)

urlpatterns = [
    path('', renderHomePageView, name='home'),
    path('newRoom/', CreateRoomView.as_view(), name='room_new'),
    path('deleteRoom/<int:pk>', DeleteRoomView.as_view(), name='room_delete'),
    path('<str:room_name>/', renderChatPageView, name='chat'),

]