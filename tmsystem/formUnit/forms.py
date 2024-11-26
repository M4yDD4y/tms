from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

class Login(forms.Form):
    login = forms.CharField(label='Логин', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')