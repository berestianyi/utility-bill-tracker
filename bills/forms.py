from datetime import datetime

from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, MonthPickerInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from bills.models import Building, BillSubCategory, Bill, BillCategory


class CustomBillForm(forms.CharField):
    pass


class BuildingForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-light',
        'placeholder': 'name@example.com,',
        'id': 'floatingInput',
        'style': 'color: #ececec; background-color: #1b1d1e'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-light',
        'placeholder': 'name@example.com,',
        'id': 'floatingInput',
        'style': 'color: #ececec; background-color: #1b1d1e'
    }))

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-light',
        'placeholder': 'Leave a comment here',
        'id': 'floatingTextarea2',
        'style': "color: #ececec; height: 100px; background-color: #1b1d1e;"
    }))

    home_mark = forms.CheckboxInput(attrs={
        'class': 'form-check-input border-light',
        'id': 'flexCheckDefault',
    })

    class Meta(object):
        model = Building
        fields = ('name', 'address', 'home_mark')


class BillsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=BillCategory.objects.all(),
                                      widget=forms.Select(attrs={
                                          "hx-get": "/load_bill_category/",
                                          "hx-target": "#id_name",
                                          "class": 'form-select',
                                          "id": "inputGroupSelect02",
                                          "style": "background-color: #1b1d1e; color: #ececec;"
                                      }))
    name = forms.ModelChoiceField(queryset=BillSubCategory.objects.none(),
                                  widget=forms.Select(attrs={
                                        "hx-get": "/load_measure_unit/",
                                        "hx-target": "#measure_unit",
                                        "class": 'form-select',
                                        "id": "id_name",
                                        "style": "background-color: #1b1d1e; color: #ececec;"}))

    amount = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Amount',
        'aria-label': "Amount",
        'style': "color: #ececec; background-color: #1b1d1e;",
        "id": "amount",
    }))

    tariff = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tariff',
        'aria-label': "Tariff",
        'style': "color: #ececec; background-color: #1b1d1e;",
        "id": "tariff",
        "value": "1"
    }))

    month_paid = forms.DateField(widget=MonthPickerInput(
        attrs={
            "class": "form-control",
            "placeholder": "Pay month",
            "type": "text",
            "style": "background-color: #1b1d1e; color: #ececec;"
        },
        options={
            "format": "MM-YYYY",
        }
    ))

    created_at = forms.DateField(widget=DatePickerInput(
        attrs={
            "class": "form-control",
            "placeholder": "Pay month",
            "type": "text",
            "style": "background-color: #1b1d1e; color: #ececec;",
            "value": f"{datetime.today().strftime('%d-%m-%Y')}",
        },
        options={
            "format": "DD-MM-YYYY",
        }
    ))

    class Meta(object):
        model = Bill
        fields = ['name', 'amount', 'tariff', 'month_paid', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "category" in self.data:
            category_id = int(self.data["category"])
            self.fields['name'].queryset = BillSubCategory.objects.filter(bill_category=category_id)
