from django.contrib import admin
from .models import Book, Author

class AuthorList(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    
class BookList(admin.ModelAdmin):
    list_display = ("title", "get_authors", "year")

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.author.all()])  # Получаем всех авторов книги

    get_authors.short_description = "Author"

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)

