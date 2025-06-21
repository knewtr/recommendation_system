from django.urls import path

from books.apps import BooksConfig
from books.views import (AuthorCreateView, AuthorDeleteView, AuthorDetailView,
                         AuthorListView, AuthorUpdateView, BookCreateView,
                         BookDeleteView, BookDetailView, BookListView,
                         BookUpdateView, GenreCreateView, GenreDeleteView,
                         GenreDetailView, GenreListView, GenreUpdateView,
                         HomeView, StatisticsView)

app_name = BooksConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
    # books
    path("books/list/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/create/", BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    # authors
    path("authors/", AuthorListView.as_view(), name="author_list"),
    path("authors/create/", AuthorCreateView.as_view(), name="author_create"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author_detail"),
    path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author_update"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author_delete"),
    # genres
    path("genres/", GenreListView.as_view(), name="genre_list"),
    path("genres/create/", GenreCreateView.as_view(), name="genre_create"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("augenres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre_update"),
    path("authors/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre_delete"),
]
