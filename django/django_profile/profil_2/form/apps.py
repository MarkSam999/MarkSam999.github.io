from django.apps import AppConfig
from .views import profile


class FormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'form'

def ready(self):
    import form.signals
