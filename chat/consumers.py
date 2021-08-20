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
        message = text_data_object['message']

        await self.channel_layer.group_send(
            self.chat_room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(
            {'message': message}
        ))
        print(json.dumps(event))
