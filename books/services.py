from books.models import Book


def get_books_by_author(author_last_name):
    "Функция возвращает список книг по фамилии автора"
    books = Book.objects.filter(author=author_last_name)
    return books


def get_books_by_genre(genre_name):
    "Функция возвращает список книг по заданному жанру"
    books = Book.objects.filter(genre=genre_name)
    return books
