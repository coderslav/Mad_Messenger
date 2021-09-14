from django.shortcuts import render, redirect, reverse
from .models import Message, User, Room
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from chat.serializers import DetailUserSerializer, PublicRoomsSerializer
from django.contrib.auth.decorators import login_required
from chat.api_permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'chat/index.html', {})


@login_required
def chat_room(request, chat_room_name):
    messages = Message.objects.filter(room__name=chat_room_name).filter(is_private=False)  # можно добавить кол-во сообщений через индексирование
    username_str = request.user.username
    return render(request, 'chat/chat_room.html', {
        'chat_room_name': chat_room_name,
        'chat_messages': messages,
        'username_str': username_str
    })


@login_required
def private_room(request, private_room_name):
    participant_1_name, participant_2_name = private_room_name.split('.')
    if request.user.username != participant_1_name and request.user.username != participant_2_name:
        return redirect(reverse('index'))
    alter_private_room_name = f'{participant_2_name}.{participant_1_name}'
    if Room.objects.filter(name=private_room_name).filter(message__is_private=True).exists():
        messages = Message.objects.filter(room__name=private_room_name).filter(is_private=True).order_by('date')
    elif Room.objects.filter(name=alter_private_room_name).filter(message__is_private=True).exists():
        return redirect(reverse('private_room', args=[alter_private_room_name]))
    else:
        messages = []
    username_str = request.user.username

    return render(request, 'chat/private_room.html', {
        'private_room_name': private_room_name,
        'chat_messages': messages,
        'talker_1': User.objects.get(username=participant_1_name),
        'talker_2': User.objects.get(username=participant_2_name),
        'username_str': username_str
    })


class DetailUserViewAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = DetailUserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class GetCurrentUserViewAPI(RetrieveAPIView):
    serializer_class = DetailUserSerializer

    def get_object(self):
        return self.request.user


class GetPublicRoomsViewAPI(ListAPIView):
    queryset = Room.objects.exclude(message__is_private=True)
    serializer_class = PublicRoomsSerializer


class GetPublicRoomsOfUserViewAPI(ListAPIView):
    lookup_field = 'username'
    serializer_class = PublicRoomsSerializer

    def get_queryset(self):
        return Room.objects.filter(participants__username=self.kwargs['username'])
