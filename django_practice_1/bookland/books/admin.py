from django.contrib import admin
from .models import Book, Author

class BookList(admin.ModelAdmin):
    list_display = ("title", "author.name", "year")

class AuthorList(admin.ModelAdmin):
    authors = ("name", "birth_date")

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)