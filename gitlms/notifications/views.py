from django.shortcuts import render
from .models import Notification


# Create your views here.
def notifications(request):
    notifications = Notification.objects.filter(recievers=request.user)
    context={'notifications':notifications}
    return render(request,"notifications.html",context)