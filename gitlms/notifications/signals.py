from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from .models import Notification

@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        group_name = f"user_{instance.reciever.id}_notifications"
        message = {
            'message': instance.message
        }

        channel_layer.group_send(
            group_name,
            {
                'type': 'send_notification',
                'message': message
            }
        )
        
