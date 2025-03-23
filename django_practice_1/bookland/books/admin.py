from django.contrib import admin
from .models import Book, Author

class BookList(admin.ModelAdmin):
    list_display = {""}

admin.site.register(Book)
admin.site.register(Author)