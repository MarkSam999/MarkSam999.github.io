from django.apps import AppConfig
from .views import profile

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

def ready()
