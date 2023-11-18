from django.contrib import admin

from .models import Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'biography']
    search_fields = ['name', 'biography']
    list_filter = ['birth_date']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'reviewer_name']
    search_fields = ['title', 'author__name', 'reviewer_name', 'content']
    list_filter = ['rating', 'author']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
