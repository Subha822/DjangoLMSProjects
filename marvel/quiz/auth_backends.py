# your_project/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from .models import Customer
from django.contrib.auth.hashers import check_password  # To check the hashed password

class CustomerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Try to find the customer by email (or username if you're using that instead)
            customer = Customer.objects.get(email=username)
            if customer.is_active and password == customer.password:  # Check password hash
                return customer
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(id=user_id)
        except Customer.DoesNotExist:
            return None
