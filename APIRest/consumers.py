# consumers.py en APIRest
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ObjectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envía el mensaje de vuelta al cliente
        await self.send(text_data=json.dumps({
            'message': message
        }))
