from asyncio import events
from unicodedata import category
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from shop.models import CustomerProfile, Order, VendorProfile, Categories, Events, Order


class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


class VendorSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_vendor']

        widgets = {
            'is_vendor': forms.CheckboxInput(attrs={'hidden': '', 'checked': ''}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        exclude = ['user', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class VendorProfileForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    events = forms.ModelMultipleChoiceField(queryset=Events.objects.all())

    class Meta:
        model = VendorProfile
        fields = '__all__'
        exclude = ['user', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'BIO', 'rows': '5'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user', "orderPlacedTime", "price", 'vendor']

        widgets = {
            'orderDeliveryTime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': "datetime-local"}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': '2'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '2'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
