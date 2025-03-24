from django.contrib import admin
from .models import Book, Author
class AuthorList(admin.ModelAdmin):
    authors = ("name", "birth_date")
    
class BookList(admin.ModelAdmin):
    list_display = ("title", str(author), "year")

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)