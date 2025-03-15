from django.urls import path
from .views import *

urlpatterns = [
    path('chats/', chats_view,  name='chats'),
]