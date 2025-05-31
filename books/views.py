from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from books.forms import AuthorForm, BookForm, GenreForm
from books.models import Author, Book, Genre
from books.services import get_books_by_author, get_books_by_genre, get_statistics


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "author_form.html"
    success_url = reverse_lazy("books:author_list")


class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = "author_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context["books"] = get_books_by_author(pk)
        return context


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm

    def get_success_url(self):
        return reverse_lazy("books:author_detail", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return AuthorForm
        raise PermissionDenied


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("books:author_list")

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return AuthorForm
        raise PermissionDenied


class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "genre_form.html"
    success_url = reverse_lazy("books:genre_list")


class GenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = "genre_list.html"


class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = "genre_detail.html"
    context_object_name = "genre"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context["books"] = get_books_by_genre(pk)
        return context


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = Genre
    form_class = GenreForm

    def get_success_url(self):
        return reverse_lazy("books:genre_detail", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return GenreForm
        raise PermissionDenied


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy("books:genre_list")

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return GenreForm
        raise PermissionDenied


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_form.html"
    success_url = reverse_lazy("books:book_list")

    def form_valid(self, form):
        book = form.save()
        user = self.request.user
        book.owner = user
        book.save()
        return super().form_valid(form)


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_form.html"
    success_url = reverse_lazy("books:book_list")

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


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StatisticsView(TemplateView):
    template_name = "statistics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statistics_data = get_statistics()
        context.update(statistics_data)

        return context
