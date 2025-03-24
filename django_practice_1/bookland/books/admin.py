from django.contrib import admin
from .models import Book, Author
class AuthorList(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    
class BookList(admin.ModelAdmin):
    list_display = ("title", "author", "year")

    def author(self, obj):
        return ", ".join(author.name for author in obj.authors.all())
    
    display_authors.short_description = "Авторы"

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)