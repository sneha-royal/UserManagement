from django import forms
from .models import User
import re

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

    # Custom validation for first name
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("First name should contain only alphabetic characters.")
        if len(first_name) < 2:
            raise forms.ValidationError("First name should be at least 2 characters long.")
        return first_name

    # Custom validation for last name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("Last name should contain only alphabetic characters.")
        if len(last_name) < 2:
            raise forms.ValidationError("Last name should be at least 2 characters long.")
        return last_name

    # Custom validation for phone number
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d{10}$', phone_number):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

    # Custom validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists.")
        return email

    # Custom validation for address
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 10:
            raise forms.ValidationError("Address should be at least 10 characters long.")
        if len(address) > 100:
            raise forms.ValidationError("Address should not exceed 100 characters.")
        return address
