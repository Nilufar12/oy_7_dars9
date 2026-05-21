from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akaunt muvafaqqiyatli ochildi!")
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
            'form': form
        }
    return render(request, 'user/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.warning(request, 'Siz akauntdan chiqyapsiz!')
    return redirect('login')