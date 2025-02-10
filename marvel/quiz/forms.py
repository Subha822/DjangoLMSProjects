from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'password','phone_number']
        widgets = {
            'password': forms.PasswordInput()
        }