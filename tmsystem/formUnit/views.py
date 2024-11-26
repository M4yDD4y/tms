from django.shortcuts import render
from django.http import HttpRequest
from django.forms import ValidationError
from .forms import Login
from django.contrib import auth

# Create your views here.

def login(request: HttpRequest):
    if request.method == 'POST':
        loginForm = Login(request.POST)
        if loginForm.is_valid():
            user = auth.authenticate(request, username=loginForm.cleaned_data['login'],
                                     password=loginForm.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return render(request, 'index.html')
            else:
                loginForm.add_error(None, ValidationError('Ошибка логина или пароля.'))
                return render(request, 'login.html',
                              {'form': loginForm})
    else:
        loginForm = Login()
    return render(request, 'login.html',
                  {"form": loginForm})

def index(request: HttpRequest):
    return render(request, 'index.html')