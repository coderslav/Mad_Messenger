from django.urls import path
from chat.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<str:chat_room_name>/', chat_room, name='chat_room'),
    path('user/create/', CreateChatUserViewAPI.as_view(), name='create_user_api'),

]