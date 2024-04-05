from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from bills.models import Building


class BuildingForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={''}))
    address = forms.CharField(widget=forms.TextInput(attrs={''}))
    add_category = forms.CharField(widget=forms.TextInput(attrs={''}))

