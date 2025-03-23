from django.contrib import admin
from .models import Book, Author

class BookList(admin.ModelAdmin):
    list_display = {"title", "author", "year"}

admin.site.register(Book, BookList)
admin.site.register(Author)