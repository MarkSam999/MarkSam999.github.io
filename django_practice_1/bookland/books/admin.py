from django.contrib import admin
from .models import Book, Author

class BookList(model.Admin)

admin.site.register(Book)
admin.site.register(Author)