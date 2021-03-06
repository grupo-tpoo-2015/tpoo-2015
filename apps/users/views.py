from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as perform_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout_then_login


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form['username'].value(),
                password=form['password1'].value(),
            )
            perform_login(request, new_user)
            return redirect('load')
    return render(request, 'users/register.jinja', {
        'form': form,
    })


def login(request):
    return render(request, 'users/login.jinja')


def logout(request):
    return logout_then_login(request)
