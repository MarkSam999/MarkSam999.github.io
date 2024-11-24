from django.contrib import admin
from .models import News_Post
from .models import Hist_Event

admin.site.register(News_Post)
admin.site.register(Hist_Event)