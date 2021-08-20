from django.shortcuts import render
from chat.models import *
from rest_framework import generics
from chat.serializers import *


def index(request):
    return render(request, 'chat/index.html', {})


def chat_room(request, chat_room_name):
    return render(request, 'chat/chat_room.html', {
        'chat_room_name': chat_room_name
    })


class CreateChatUserViewAPI(generics.CreateAPIView):
    serializer_class = ChatUserDetailsSerializer
