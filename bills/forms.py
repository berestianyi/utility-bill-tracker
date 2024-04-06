from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from bills.models import Building, BillSubCategory


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

    description = forms.CharField(widget=forms.Textarea(attrs={
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
