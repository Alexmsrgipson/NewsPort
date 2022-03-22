from django.apps import AppConfig


class ProvitoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'provito'

    def ready(self):
        from .signals import send_message
