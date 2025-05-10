from . import views
from django.urls import path

urlpatterns = [
    path('math_question', views.math_question_view, name='math_question'),
    path('success', views.success, name='success')
]