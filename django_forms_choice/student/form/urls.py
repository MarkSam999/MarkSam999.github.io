from . import views
from django.urls import path

urlpatterns = [
    path('', views.choice_form, name='choice.form')
]