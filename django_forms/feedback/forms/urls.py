from . import views
from django.urls import path

urlpatterns = [
    path('form/', views.feedback, name='feedback'),
    path('list/', views.reviews, name="review_list")
]