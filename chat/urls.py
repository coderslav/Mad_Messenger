from django.urls import path
from chat.views import index, chat_room, private_room, DetailUserViewAPI, GetCurrentUserViewAPI, GetPublicRoomsViewAPI

urlpatterns = [
    path('', index, name='index'),
    path('<str:chat_room_name>/', chat_room, name='chat_room'),
    path('private/<str:private_room_name>/', private_room, name='private_room'),
    # API
    path('api/v1/accounts/detail/<str:username>', DetailUserViewAPI.as_view(), name='detail_user_api'),
    path('api/v1/accounts/get_user/', GetCurrentUserViewAPI.as_view(), name='get_current_user_api'),
    path('api/v1/get_public_rooms/', GetPublicRoomsViewAPI.as_view(), name='get_public_rooms_api'),
]
