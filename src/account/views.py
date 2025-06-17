from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = User.objects.create_user(username=username, password=password1)
        user = authenticate(username=username, password=password1)
        if user:
            auth_login(request, user)
            print("user created")
            return redirect("checkout")
        else:
            return render(request, 'registration/signup.html')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect("checkout")
    return render(request, 'registration/login.html')

def logout(request):
    auth_logout(request)
    return redirect('product_list')