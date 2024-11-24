from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('news/', views.news, name='news'),
    path('game_map/', views.game_map, name='game_map'),
    path('statistics/', views.statistics, name='statistics'),
    path('chat/', views.chat, name='chat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)