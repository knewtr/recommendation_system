from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from books.forms import StyleFormMixin
from books.models import Author, Genre
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    favourite_genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "genre-selector",
            }
        ),
        required=False,
        label="Любимые жанры",
    )
    favourite_author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "author-selector",
            }
        ),
        required=False,
        label="Любимые fdnjhs",
    )

    class Meta:
        model = User
        fields = (
            "email",
            "avatar",
            "favourite_book",
            "favourite_author",
            "favourite_genre",
            "password1",
            "password2",
        )


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="email")


class UserUpdateForm(StyleFormMixin, UserCreationForm):
    favourite_genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "genre-selector",
            }
        ),
        required=False,
        label="Любимые жанры",
    )
    favourite_author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "author-selector",
            }
        ),
        required=False,
        label="Любимые авторы",
    )

    class Meta:
        model = User
        fields = (
            "avatar",
            "favourite_book",
            "favourite_author",
            "favourite_genre",
        )
