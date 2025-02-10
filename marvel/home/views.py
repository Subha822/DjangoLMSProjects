from django.http import HttpResponse
from quiz.models import Customer  # Import Customer model from quiz app
from quiz.forms import CustomerForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    return  render(request,'home/index.html')

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'customer/login.html', {'error': 'Invalid credentials'})
    return render(request, 'customer/login.html')

# Register view
def register_view(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerForm()
    return render(request, 'customer/register.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')