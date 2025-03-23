from django.contrib import admin
from .models import Book, Author

class BookList(admin.ModelAdmin):
    list_display = {"title", "author", "year"}

class AuthorList(admin.ModelAdmin):
    authors = 

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorL