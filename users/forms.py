from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # 如果使用默认User则替换为`from django.contrib.auth.models import User`

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # 或 User
        fields = ["username", "email", "password1", "password2"]