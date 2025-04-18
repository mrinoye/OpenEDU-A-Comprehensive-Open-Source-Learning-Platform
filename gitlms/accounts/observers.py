from django.contrib import messages
from abc import ABC, abstractmethod

# observers.py
class UserProfileUpdatedObserver:
    def update(self,request, user):
        messages.success(request,f"{user.first_name} {user.last_name}'s profile has been updated")

class SessionObserver(ABC):
    @abstractmethod
    def session_created(self, user, session_data):
        pass

    @abstractmethod
    def session_accessed(self, user, session_data):
        pass

class SessionLogger(SessionObserver):
    def session_created(self, user, session_data):
        print(f"New session created for {user.username} from {session_data['device']}")

    def session_accessed(self, user, session_data):
        print(f"Session accessed for {user.username} from {session_data['device']}")

class SessionAnalytics(SessionObserver):
    def session_created(self, user, session_data):
        # Example: Send to analytics service
        print(f"[Analytics] Session created - User: {user.id}, Device: {session_data['device']}")

    def session_accessed(self, user, session_data):
        # Example: Update analytics
        print(f"[Analytics] Session accessed - User: {user.id}, IP: {session_data['location']}")