from django.db.models import Count

from books.models import Book
from users.models import User


def get_books_by_author(author_last_name):
    "Функция возвращает список книг по фамилии автора"
    books = Book.objects.filter(author=author_last_name)
    return books


def get_books_by_genre(genre_name):
    "Функция возвращает список книг по заданному жанру"
    books = Book.objects.filter(genre=genre_name)
    return books


def get_statistics():
    books_count = Book.objects.all().count()
    users_count = User.objects.all().count()

    top_books = Book.objects.annotate(
        rating_count=Count("connection__rating")
                           ).order_by("-rating", "-rating_count")[:5]

    statistics_data = {
    "books_count": books_count,
    "users_count": users_count,
    "top_books": top_books,
    }

    return statistics_data