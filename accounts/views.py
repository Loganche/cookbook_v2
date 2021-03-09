from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from .forms import CreateUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:home')
            else:
                messages.info(request, 'Username or password is incorrect.')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required(login_url='accounts:login')
def users(request):
    return render(request, 'accounts/users.html')
