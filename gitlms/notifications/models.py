from django.db import models
from accounts.models import User

class Notification(models.Model):
    recievers = models.ManyToManyField(User, related_name="notifications")
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    type=models.CharField(max_length=6)
    content_id= models.IntegerField(default=0, null=True, blank=True)
    real_content_id=models.IntegerField(default=0, null=True, blank=True)
    type=models.CharField(max_length=10)
    content_type=models.CharField(max_length=15)
    def __str__(self):
        return f"Notification from {self.sender.username}: {self.message}"
