from django.contrib import messages
# observers.py
class UserProfileUpdatedObserver:
    def update(self,request, user):
        messages.success(request,f"{user.first_name} {user.last_name}'s profile has been updated")
