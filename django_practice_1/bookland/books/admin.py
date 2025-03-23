from django.contrib import admin
from .models import Book, Author

class BookList(admin.AdminModel)

admin.site.register(Book)
admin.site.register(Author)