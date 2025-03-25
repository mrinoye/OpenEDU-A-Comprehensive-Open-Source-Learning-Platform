from django.db import models
from accounts.models import User

class Notification(models.Model):
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    type=models.CharField(max_length=6)
    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"
