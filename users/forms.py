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

    class Meta:
        model = User
        fields = (
            "email",
            "avatar",
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

    class Meta:
        model = User
        fields = (
            "avatar",
            "favourite_genre",
        )
