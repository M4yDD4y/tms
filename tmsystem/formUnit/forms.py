from django import forms

class Login(forms.Form):
    login = forms.CharField(label='Логин', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')