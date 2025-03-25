import json

from channels.generic.websocket import AsyncWebsocketConsumer



class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.debug(f"WebSocket connection attempt by user: {self.scope.get('user', 'Anonymous')}")

        try:
            # Get the user id (you can get this from the session, JWT, etc.)
            self.user_id = self.scope['user'].id
            self.room_group_name = f"user_notifications_{self.user_id}"

            logger.debug(f"User ID: {self.user_id}, Room Group: {self.room_group_name}")

            # Join the room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            logger.debug("Successfully joined room group.")
            await self.accept()
            logger.debug("WebSocket connection accepted.")
        except Exception as e:
            logger.error(f"Error during WebSocket connection: {e}")
            await self.close()

    async def disconnect(self, close_code):
        logger.debug(f"WebSocket disconnected with code: {close_code}")

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        logger.debug(f"Received data: {text_data}")

    async def send_notification(self, event):
        notification = event['notification']
        await self.send(text_data=json.dumps({
            'notification': notification
        }))
