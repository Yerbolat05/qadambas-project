from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from auths.models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )

class CustomUserForm(forms.ModelForm):
    email = forms.EmailField()
    login = forms.CharField(
        widget = forms.TextInput
    )
    password = forms.CharField(
        widget = forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'login',
            'password'
            
        )