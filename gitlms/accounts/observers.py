# observers.py
class UserProfileUpdatedObserver:
    def update(self, user):
        # Here you can send an email, log the update, or notify the system
        print(f"Profile updated for {user.username}")
