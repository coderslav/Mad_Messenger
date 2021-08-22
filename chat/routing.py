from django.urls import re_path, path
from chat.consumers import ChatRoomConsumer

# websocket_urlpatterns = [
#     re_path(r'^ws/chat/(?P<chat_room_name>\w+)/$', ChatRoomConsumer.as_asgi())
# ]

websocket_urlpatterns = [
    path('ws/chat/<str:chat_room_name>/', ChatRoomConsumer.as_asgi())
]
