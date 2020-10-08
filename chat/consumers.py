import json
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Room
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.message_user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_body = text_data_json['messageBody']
        room = Room.objects.get(room=self.room_name)
        message = Message.objects.create(body=message_body, user=self.message_user, room=room)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'message',
                'messageBody': message.body,
                'messageUser': self.message_user.username,
                'messageDate': message.date.isoformat(),
            }
        )

    def message(self, event):
        self.send(text_data=json.dumps({
            'messageBody': event['messageBody'],
            'messageUser': event['messageUser'],
            'messageDate': event['messageDate'],
        }))


