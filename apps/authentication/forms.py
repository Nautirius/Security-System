from allauth.account.forms import SignupForm
from django import forms
from django.http import HttpRequest

from apps.authentication.models import UserProfile


class CustomSignupForm(SignupForm):
    firstname = forms.CharField(
        max_length=30,
        label="Firstname",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter First Name"
        })
    )
    lastname = forms.CharField(
        max_length=30,
        label="Lastname",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter Last Name"
        })
    )
    phone = forms.CharField(
        max_length=15,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter phone number"
        })
    )
    street = forms.CharField(
        max_length=255,
        label="Street",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter street"
        })
    )
    city = forms.CharField(
        max_length=100,
        label="City",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter city"
        })
    )
    zip_code = forms.CharField(
        max_length=10,
        label="ZIP Code",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter ZIP Code"
        })
    )

    def save(self, request: HttpRequest) -> UserProfile:
        user = super().save(request)

        profile, created = UserProfile.objects.get_or_create(user=user)

        profile.first_name = request.POST['firstname']
        profile.last_name = request.POST['lastname']
        profile.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.street = request.POST['street']
        profile.city = request.POST['city']
        profile.zip_code = request.POST['zip_code']
        profile.save()

        return user