import re
from django.contrib import messages
from django.shortcuts import render, redirect


from .forms import CreateUserForm
from app.models import Cart
from django.contrib.auth import authenticate, login, logout

# from .forms import AddressForm

# Create your views here.

def signup(request):
    form =  CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account Created! You can Login')
            return redirect('signin')
    
    context = {'form': form}
    return render(request, 'UserProfile/signup.html', context)

def signin(request):
    print("sdfdas53245234523")
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next') or 'product'
            print("next_url:", next_url)
            messages.success(request, 'Login successful')
            return redirect(next_url)
        else:
            messages.info(request, 'Invalid credentials')

    return render(request, 'registration/login.html', {'next': request.GET.get('next', '')})

def signout(request):
    logout(request)
    return redirect('index')

# def changeAddress(request):
#     customer = request.user.customer
#     address = Address.objects.get(customer=customer)
#     form = AddressForm(instance=address)
#     if request.method == 'POST':
#         form = AddressForm(request.POST,instance=address)
#         if form.is_valid():
#             new_address = form.save(commit=False)
#             new_address.customer = customer
#             new_address.save()
#             return redirect('checkout')
#     context = {'form':form}
#     return render(request, 'UserProfile/updateaddress.html', context)
    