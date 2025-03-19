from django.contrib.auth.hashers import make_password
from .models import User

def create_user(email, password, first_name, last_name,username):
    user = User(email=email, first_name=first_name, last_name=last_name,username=username)
    user.set_password(password)
    user.save()
    return user

class RegistrationStrategy:
    def register(self, data):
        raise NotImplementedError

class RegularUserRegistration(RegistrationStrategy):
    def register(self, data):
        # Regular user registration logic
        return create_user(email=data['email'], password=data['passw'], first_name=data['fname'], last_name=data['lname'],username=data['email'])

class AdminUserRegistration(RegistrationStrategy):
    def register(self, data):
        # Admin registration logic
        user = create_user(email=data['email'], password=data['passw'], first_name=data['fname'], last_name=data['lname'],username=data['email'])
        user.is_admin = True
        user.save()
        return user
