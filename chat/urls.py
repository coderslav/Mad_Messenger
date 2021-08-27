from django.urls import path
from chat.views import index, chat_room, private_room, CreateChatUserViewAPI

urlpatterns = [
    path('', index, name='index'),
    path('<str:chat_room_name>/', chat_room, name='chat_room'),
    path('private/<str:private_room_name>/', private_room, name='private_room'),
    path('user/create/', CreateChatUserViewAPI.as_view(), name='create_user_api'),

]