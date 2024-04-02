from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter your password"}))

    class Meta:
        model = User
        fields = ('username', 'password')