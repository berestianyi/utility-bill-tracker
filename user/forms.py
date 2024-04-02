from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user.models import User


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': "Enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter your password"}))

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': "Enter your email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Create password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Repeat password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = User
        fields = ('username', 'email')
