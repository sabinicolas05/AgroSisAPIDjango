from channels.layers import get_channel_layer
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TipoEspecieConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_layer = get_channel_layer()
        await self.channel_layer.group_add(
            "objects_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """Cuando un cliente se desconecta"""
        # El cliente se elimina del grupo
        await self.channel_layer.group_discard(
            "objects_group",  # El nombre del grupo
            self.channel_name
        )

    async def nuevo_objeto(self, event):
        """Cuando se recibe una señal de creación o actualización de un objeto"""
        message = event["message"]  # El mensaje que viene del emisor

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            "message": message  # Aquí el cliente recibirá el mensaje
        }))
