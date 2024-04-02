from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user.models import User


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': "name@example.com",
        'type': "email",
        'id': "floatingInput",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
        'type': "password",
        'id': "floatingPassword",
    }))

    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-primary'
            field.widget.attrs['style'] = 'background-color: #222049; color: #ececec;'


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your username",
        'id': "floatingInput",
        'type': "text",

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': "name@example.com",
        'type': "email",
        'id': "floatingInput",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
        'type': "password",
        'id': "floatingPassword",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
        'type': "password",
        'id': "floatingPassword",
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-success'
            field.widget.attrs['style'] = 'background-color: #0b3817; color: #ececec;'


class UserProfileChangeForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'readonly': True,
        'placeholder': "name@example.com",
        'type': "email",
        'id': "floatingInput",
    }))

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UserProfileChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-info'
            field.widget.attrs['style'] = 'background-color: #1b4757; color: #ececec;'
