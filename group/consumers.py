
import json
from user.models import *
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.template.loader import render_to_string
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"


        await self.channel_layer.group_add(
             self.room_group_name,
             self.channel_name
            )

        await self.send({
            'type':'websocket.accept'
        })

    ##################################################################

    async def websocket_receive(self,event):
        data = json.loads(event['text'])
        message = data["message"]
        user_id=str(data['user_id'])
        status=str(data['status'])
        group_id=str(self.room_name)
        chat=Chat_message(
            msg=message,
            post_typing_status=status,
            group_id=group_id,
            user_id=user_id,
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
             self.room_group_name,
             {
                 'type':'chat.message',
                 'message':event['text']
             }
        )

    #----------------------------

    async def chat_message(self, event):
        await self.send({
            'type':'websocket.send',
            'text':event['message'],
        })


    ###################################################################

    async def websocket_disconnect(self,event):
        await async_to_sync(self.channel_layer.group_discard)(
             self.room_group_name,
             self.channel_name
        )
        raise StopConsumer()

