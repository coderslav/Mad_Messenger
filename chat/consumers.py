from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_room_name = self.scope['url_route']['kwargs']['chat_room_name']
        self.chat_room_group_name = f'chat_{self.chat_room_name}'
        await self.channel_layer.group_add(
            self.chat_room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.chat_room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        text_data_object = json.loads(text_data)
        author = text_data_object['author']
        message = text_data_object['message']
        time = text_data_object['time']
        room = text_data_object['room']
        count = text_data_object['count']

        await self.channel_layer.group_send(
            self.chat_room_group_name,
            {
                'type': 'chat_message',
                'author': author,
                'message': message,
                'time': time,
                'room': room,
                'count': count
            }
        )

    async def chat_message(self, event):
        author = event['author']
        message = event['message']
        time = event['time']
        room = event['room']
        count = event['count']
        await self.send(text_data=json.dumps(
            {
                'author': author,
                'message': message,
                'time': time,
                'room': room,
                'count': count
             }
        ))
        print(json.dumps(event))
