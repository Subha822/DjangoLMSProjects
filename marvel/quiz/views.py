from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm

# Create your views here.
def index(request):
    return render(request,'quiz/index.html')

# Create
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
    else:
        form = CustomerForm()
    return render(request, 'customers/create_customer.html', {'form': form})

# Read
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list_customers.html', {'customers': customers})

# Update
def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
    else:
        form = CustomerForm(instance=customer)
        print("ssdfsfs", form)
    return render(request, 'customers/update_customer.html', {'form': form})

# Delete
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('list_customers')
    return render(request, 'customers/delete_customer.html', {'customer': customer})
