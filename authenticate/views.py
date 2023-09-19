from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistration

from django.contrib.auth.decorators import login_required

# Create your views here.

def Registration_page(request):

    forms = UserRegistration()
    if request.method == 'POST':
        forms = UserRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')

    context = {
        'forms': forms
    }

    return render(request, 'registration.html', context)


def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

@login_required(login_url='login')
def Home_page(request):
    return render(request, 'home.html')

def logout_page(request):
    logout(request)
    return redirect('login');


