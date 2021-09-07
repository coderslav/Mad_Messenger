from django.shortcuts import render, redirect, reverse
from .models import Message, User, Room
from rest_framework import generics
from chat.serializers import ChatUserDetailsSerializer
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/index.html', {})


def chat_room(request, chat_room_name):
    messages = Message.objects.filter(room__name=chat_room_name).filter(is_private=False)  # можно добавить кол-во сообщений через индексирование
    if not request.user.username:
        username_str = 'Anonymous'
    else:
        username_str = request.user.username
    return render(request, 'chat/chat_room.html', {
        'chat_room_name': chat_room_name,
        'messages': messages,
        'username_str': username_str
    })


@login_required
def private_room(request, private_room_name):
    participant_1_name, participant_2_name = private_room_name.split('.')
    # TODO Деактивировать тестовый код в следующем TODO после тестов. И активировать закомментированный код:
    # if request.user.username != participant_1_name and request.user.username != participant_2_name:
    #     return redirect(reverse('index'))
    alter_private_room_name = f'{participant_2_name}.{participant_1_name}'
    if Room.objects.filter(name=private_room_name).filter(message__is_private=True).exists():
        messages = Message.objects.filter(room__name=private_room_name).filter(is_private=True).order_by('date')
    elif Room.objects.filter(name=alter_private_room_name).filter(message__is_private=True).exists():
        return redirect(reverse('private_room', args=[alter_private_room_name]))
    else:
        messages = []
    # TODO следующий код только для теста. После теста удалить и заменить проверкой юзера делающего запрос:
    if not request.user.username:
        username_str = 'Anonymous'
    else:
        username_str = request.user.username
    # TODO конец тестового кода

    return render(request, 'chat/private_room.html', {
        'private_room_name': private_room_name,
        'messages': messages,
        'talker_1': User.objects.get(username=participant_1_name),
        'talker_2': User.objects.get(username=participant_2_name),
        'username_str': username_str
    })


class CreateChatUserViewAPI(generics.CreateAPIView):
    serializer_class = ChatUserDetailsSerializer
