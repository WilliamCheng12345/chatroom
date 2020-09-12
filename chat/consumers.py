import json
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Room
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.messageUser = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        self.chatroom_group_name = self.chatroom_name

        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        print(code)
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        messageBody = text_data_json['messageBody']
        room, created = Room.objects.get_or_create(room=self.chatroom_name, slug=self.chatroom_name)
        message = Message.objects.create(body=messageBody, user=self.messageUser, room=room)

        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_group_name,
            {
                'type': 'chat.message',
                'messageBody': message.body,
                'messageUser': self.messageUser.username,
                'messageDate': message.date.isoformat(),
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'messageBody': event['messageBody'],
            'messageUser': event['messageUser'],
            'messageDate': event['messageDate'],
        }))


