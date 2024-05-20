from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from django.core.validators import RegexValidator

from .models import Building


class BuildingForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control border-light",
                "placeholder": "name@example.com,",
                "id": "floatingInput",
                "style": "color: #ececec; background-color: #1b1d1e",
            },
        ),
        max_length=50,
    )
    address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control border-light",
                "placeholder": "name@example.com,",
                "id": "floatingInput",
                "style": "color: #ececec; background-color: #1b1d1e",
            }
        )
    )

    description = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control border-light",
                "id": "TextareaDescription",
                "style": "color: #ececec; background-color: #1b1d1e;",
            }
        )
    )

    home_mark = forms.CheckboxInput(
        attrs={
            "class": "form-check-input mt-0",
            "type": "checkbox",

        }
    )

    class Meta(object):
        model = Building
        fields = ("name", "address", "home_mark", "description")
