from . import views
from django.urls import path

urlpatterns = [
    path('form/', views.feedback, name='feedback'),
    path('list', views.review_list, name="review_list"