# facade.py
from .strategies import RegularUserRegistration, AdminUserRegistration

class RegistrationFacade:
    def __init__(self):
        # Initialize strategies for regular users and admins
        self.regular_registration = RegularUserRegistration()
        self.admin_registration = AdminUserRegistration()

    def register(self, data, user_type="regular"):
        """
        A simplified interface for user registration.
        
        Parameters:
            data (dict): User data (email, passw, fname, lname)
            user_type (str): Type of user, can be "regular" or "admin"
            
        Returns:
            User object if registration is successful
        """
        if user_type == "admin":
            return self.admin_registration.register(data)
        return self.regular_registration.register(data)
