from django.urls import re_path
from chat.consumers import *

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<chat_room_name>\w+)/$', ChatRoomConsumer.as_asgi())
]
