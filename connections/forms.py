from django import forms
from django.forms import ModelForm

from books.forms import StyleFormMixin
from connections.models import Connection


class ConnectionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Connection
        fields = ["rating"]
        widgets = {"rating": forms.NumberInput(attrs={"min": 1, "max": 10, "step": 1})}
