# singleton.py
from .models import User

class UserSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, user_id=None):
        if cls._instance is None and user_id:
            cls._instance = User.objects.get(id=user_id)
        return cls._instance
