from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('game_practice/', views.play_game, name='game_practice'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)