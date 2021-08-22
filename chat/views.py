from django.shortcuts import render
from .models import Message
from rest_framework import generics
from chat.serializers import ChatUserDetailsSerializer


def index(request):
    return render(request, 'chat/index.html', {})


def chat_room(request, chat_room_name):
    messages = Message.objects.filter(room__name=chat_room_name)  # можно добавить кол-во сообщений через индексирование
    return render(request, 'chat/chat_room.html', {
        'chat_room_name': chat_room_name,
        'messages': messages
    })


class CreateChatUserViewAPI(generics.CreateAPIView):
    serializer_class = ChatUserDetailsSerializer
