from django.contrib import admin
from django.db import models
from django.forms import DateInput

from books.models import Author, Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput(format='%d.%m.%Y')},
    }
    list_display = ("id", "title")
    list_filter = ("genre",)
    search_fields = (
        "title",
        "author",
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
