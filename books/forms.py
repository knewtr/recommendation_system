from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from books.models import Author, Book, Genre

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class BookForm(StyleFormMixin, ModelForm):
    publication_date = forms.DateField(
        input_formats=["%d.%m.%Y"],
        widget=forms.DateInput(attrs={"placeholder": "ДД.ММ.ГГГГ"}),
    )

    class Meta:
        model = Book
        fields = "__all__"

    def clean_photo(self):
        max_size = 5 * 1024 * 1024
        cover = self.cleaned_data.get("cover")
        extension = cover.name.split(".")[-1].lower()
        if extension not in ALLOWED_EXTENSIONS:
            raise ValidationError("Неподходящий формат изображения")

        if cover.size > max_size:
            raise ValidationError(
                "Максимальный размер изображения не должен быть больше 5Мб"
            )

        return cover


class AuthorForm(StyleFormMixin, ModelForm):
    birth_date = forms.DateField(
        input_formats=["%d.%m.%Y"],
        widget=forms.DateInput(attrs={"placeholder": "ДД.ММ.ГГГГ"}),
    )

    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "book",
            "genre",
        ]


class GenreForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Genre
        fields = [
            "name",
            "description",
        ]
