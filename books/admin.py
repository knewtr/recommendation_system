from django.contrib import admin

from books.models import Author, Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
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
