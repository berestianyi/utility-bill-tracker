from bootstrap_datepicker_plus.widgets import MonthPickerInput
from django import forms
from django.core.validators import RegexValidator

from bills.models import Bill, BillType


class CustomBillForm(forms.CharField):
    pass


class BillsForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=BillType.objects.all(),
        widget=forms.Select(
            attrs={
                "hx-get": "/load_tariff_and_measure_unit/",
                "hx-target": "#tariff_and_measure_unit",
                "class": "form-select",
                "id": "id_name",
                "style": "background-color: #1b1d1e; color: #ececec;",
            }
        ),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='You should choose bill',
                code='invalid_name'
            )
        ]
    )

    amount = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Amount",
                "aria-label": "Amount",
                "style": "color: #ececec; background-color: #1b1d1e;",
                "id": "amount",
                "type": "number",
                "min": "0"
            }
        )
    )

    month_paid = forms.DateField(
        widget=MonthPickerInput(
            attrs={
                "class": "form-control",
                "placeholder": "Pay month",
                "type": "text",
                "style": "background-color: #1b1d1e; color: #ececec;",
            },
            options={
                "format": "MM-YYYY",
            },
        )
    )

    class Meta(object):
        model = Bill
        fields = ["name", "amount", "month_paid"]


class UploadFileBillForm(forms.ModelForm):
    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
                "type": "file",
                "id": "formFile",
                "style": "background-color: #1b1d1e; color: #ececec;",
                "name": "bill_file",
            }
        )
    )

    class Meta(object):
        model = Bill
        fields = ["file"]
