from django.urls import path

from books.apps import BooksConfig
from books.views import (AuthorDetailView, AuthorListView, BookCreateView,
                         BookDeleteView, BookDetailView, BookListView,
                         BookUpdateView, GenreDetailView, GenreListView)

app_name = BooksConfig.name

urlpatterns = [
    path("", BookListView.as_view(), name="books_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/create/", BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("authors/", AuthorListView.as_view(), name="authors_list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author_details"),
    path("genres/", GenreListView.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre_details"),
]
