from django.contrib import admin
from .models import Book, Author

class AuthorList(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    
class BookList(admin.ModelAdmin):
    list_display = ("title", str(author), "year")

    def author(self, obj):
        str(Author.objects.all().values().name)

admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)