from django.urls import path
from chat.views import index, chat_room, private_room, DetailUserViewAPI

urlpatterns = [
    path('', index, name='index'),
    path('<str:chat_room_name>/', chat_room, name='chat_room'),
    path('private/<str:private_room_name>/', private_room, name='private_room'),

    path('api/v1/accounts/detail/<str:username>', DetailUserViewAPI.as_view(), name='detail_user_api'),
]
