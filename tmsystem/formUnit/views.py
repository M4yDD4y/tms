from django.shortcuts import render
from django.http import HttpRequest
from django.forms import ValidationError
from .forms import Login
from .models import User

# Create your views here.

def login(request: HttpRequest):
    if request.method == 'POST':
        loginForm = Login(request.POST)
        if loginForm.is_valid():
            try:
                user = User.objects.get(name=request.POST.get('login'))
                if user.password == request.get('password'):
                    return render(request, 'index.html')
                else:
                    raise ValidationError('Неверный пароль.')
            except:
                raise ValidationError('Неверный логин.')
    else:
        loginForm = Login()
    return render(request, 'login.html',
                  {"form": loginForm})