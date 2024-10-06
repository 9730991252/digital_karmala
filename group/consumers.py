import json
from user.models import *
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.template.loader import render_to_string


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        user_id=str(data['user_id'])
        user_name=data['user_name']
        user_village_name=data['user_village_name']
        group_id=str(self.room_name)
        chat=Chat_message(
            msg=message,
            group_id=group_id,
            user_id=user_id,
        )
        chat.save()
        
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat.message", 
                "message":message,
                "user_name":user_name,
                "user_village_name":user_village_name,
                }
            )
    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user_name = event["user_name"]
        user_village_name = event["user_village_name"]
        context={
            'message':message,
            'user_name':user_name,
            'user_village_name':user_village_name
        }
        html = render_to_string("group/chat_message.html", context)
        print(html)
        self.send(text_data=html)
        
        
        
        
        
        

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )