from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from books.forms import BookForm
from books.models import Author, Book, Genre
from books.services import get_books_by_author, get_books_by_genre


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = "books/author_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context["books"] = get_books_by_author(pk)
        return context


class GenreListView(LoginRequiredMixin, ListView):
    model = Genre


class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = "books/genre_detail.html"
    context_object_name = "genre"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context["books"] = get_books_by_genre(pk)
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("books:book_list")

    def form_valid(self, form):
        book = form.save()
        user = self.request.user
        book.owner = user
        book.save()
        return super().form_valid(form)


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse_lazy("books:book_detail", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return BookForm
        raise PermissionDenied


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books:book_list")

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return BookForm
        raise PermissionDenied
