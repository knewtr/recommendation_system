from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    avatar = forms.ImageField(
        required=False, help_text="Загрузите аватар (необязательно)"
    )
    favourite_book = forms.CharField(
        max_length=150, required=False, help_text="Укажите любимую книгу"
    )
    favourite_author = forms.CharField(
        max_length=150, required=False, help_text="Укажите любимого автора"
    )
    favourite_genre = forms.CharField(
        max_length=150, required=False, help_text="Укажите любимый жанр"
    )

    class Meta(UserCreationForm.Meta):
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


class UserUpdateForm(ModelForm):
    password = None

    class Meta(UserChangeForm):
        model = User
        fields = ("avatar", "favourite_book", "favourite_author", "favourite_genre")
