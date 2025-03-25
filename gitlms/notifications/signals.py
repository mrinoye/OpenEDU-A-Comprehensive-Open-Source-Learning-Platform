from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from .models import Notification

@receiver(post_save, sender=Notification)
def send_notification_signal(sender, instance, created, **kwargs):
    if created:  # Only send notification when a new one is created
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{instance.user.id}",  # Send to the specific user’s WebSocket group
            {
                "type": "send_notification",
                "message": instance.message,
            },
        )
