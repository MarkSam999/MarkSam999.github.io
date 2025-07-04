"""
URL configuration for math_crusaders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import email_login_view
from users import views as user_views

urlpatterns = [
    path('mathcrusaders/admin', admin.site.urls),
    path('mathcrusaders/register/', user_views.register, name='register'),
    path('mathcrusaders/profile/', user_views.profile, name='profile'),
    path('mathcrusaders/login/', email_login_view, name='login'),
    path('mathcrusaders/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('mathcrusaders/', include('main_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
