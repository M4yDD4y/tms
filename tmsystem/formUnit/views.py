from django.shortcuts import render
from .forms import Login

# Create your views here.

def login(request):
    loginForm = Login()
    return render(request, 'login.html',
                  {"form": loginForm})