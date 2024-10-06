import json
from user.models import *
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.template.loader import render_to_string
from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"


        async_to_sync(self.channel_layer.group_add)(
             self.room_group_name,
             self.channel_name
            )
        
        self.send({
            'type':'websocket.accept'
        })

    ##################################################################

    def websocket_receive(self,event):
        async_to_sync(self.channel_layer.group_send)(
             self.room_group_name,
             {
                 'type':'chat.message',
                 'message':event['text']
             }
        )

    #----------------------------
    
    def chat_message(self, event):
        self.send({
            'type':'websocket.send',
            'text':event['message'],
            'text':event['user_name'],
        })


    ###################################################################

    def websocket_disconnect(self,event):
        print('websocket_disconnect',event)
        async_to_sync(self.channel_layer.group_discard)(
             self.room_group_name,
             self.channel_name
        )
        raise StopConsumer()


