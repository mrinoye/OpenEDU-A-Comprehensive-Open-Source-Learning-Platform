from django.apps import AppConfig


class LmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lms'

class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"

    def ready(self):
        import notifications.signals  

        


class LmsConfig(AppConfig):
    name = 'lms'

    def ready(self):
        import lms.signals  # Reuse the same signals from accounts
