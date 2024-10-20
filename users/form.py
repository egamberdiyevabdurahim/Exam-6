from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserModel


class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    organization_name = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
    linkedin_link = forms.CharField(max_length=200, required=False)
    avatar = forms.ImageField(required=False)
