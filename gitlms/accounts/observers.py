from django.contrib import messages
# observers.py
class UserProfileUpdatedObserver:
    def update(self,request, user):
        messages.success(request,"{{user.username}}'s profile has been updated")
