from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from channels.layers import get_channel_layer
from .models import Notification

@receiver(post_save, sender=Notification)
def send_notification_to_users(sender, instance, created, **kwargs):
    if created:
        # Get the channel layer
        channel_layer = get_channel_layer()

        # You can send the notification to multiple receivers
        for receiver in instance.reciever.all():
            # Generate the notification message you want to send
            notification_message = {
                'notification': instance.message,
                'sender': instance.sender.username,
                'type': instance.type,
            }
            
            # Send notification to each receiver's WebSocket group
            try:
                # Send message to the WebSocket group for that user
                channel_layer.group_send(
                    f"user_notifications_{receiver.id}",
                    {
                        'type': 'send_notification',
                        'notification': notification_message
                    }
                )
            except ObjectDoesNotExist:
                pass
