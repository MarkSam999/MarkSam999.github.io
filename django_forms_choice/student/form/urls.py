from . import views
from django.urls import path

urlpatterns = [
    path('math_question', views.generate_question, name='choice.form'),
    path('success', views.success, name='success')
]