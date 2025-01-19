from django.urls import path
from . import views
from .views import (NewsPostListView, 
                    NewsPostDetailView,
                    NewsPostCreateView,
                    NewsPostUpdateView,
                    NewsPostDeleteView,
                    RatingListView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('news/', NewsPostListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsPostDetailView.as_view(), name='news_post'),
    path('news/<int:pk>/edit', NewsPostUpdateView.as_view(), name='news_post_edit'),
    path('news/<int:pk>/delete', NewsPostDeleteView.as_view(), name='news_post_delete'),
    path('news/new/', NewsPostCreateView.as_view(), name='news_post_add'),
    path('arena/', views.arena, name='arena'),
    path('rating/', RatingListView.as_view(), name='rating'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('news/', NewsPostListView.as_view(), name='news'),
    path('game_map/', views.game_map, name='game_map'),
    path('statistics/', views.statistics, name='statistics'),
    path('chat/', views.chat, name='chat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)