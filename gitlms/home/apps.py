from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import lms.signals  # Ensure signals are loaded
