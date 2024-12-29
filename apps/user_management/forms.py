from typing import Tuple

from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.http import HttpRequest

from apps.authentication.models import UserProfile


class CreateUserManagementForm(SignupForm):
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
    company = forms.CharField(
        max_length=10,
        label="Company",
        widget=forms.TextInput(attrs={
            "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm",
            "placeholder": "Enter company name"
        })
    )

    def save(self, request: HttpRequest) -> Tuple[User,UserProfile]:
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

        company_name = request.POST['company']

        return user,profile





class UpdateUserManagementForm(forms.Form):
    firstname = forms.CharField(
        max_length=30,
        label="Firstname",
    )
    lastname = forms.CharField(
        max_length=30,
        label="Lastname",
    )
    email = forms.CharField(
        max_length=100,
        label="Email",
    )
    phone = forms.CharField(
        max_length=50,
        label="Phone Number",
    )
    street = forms.CharField(
        max_length=255,
        label="Street",
    )
    city = forms.CharField(
        max_length=100,
        label="City",
    )
    zip_code = forms.CharField(
        max_length=10,
        label="ZIP Code",
    )
    company = forms.CharField(
        max_length=100,
        label="Company",
    )

    def __init__(self, *args, user: User = None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields['firstname'].initial = user.profile.first_name
            self.fields['lastname'].initial = user.profile.last_name
            self.fields['email'].initial = user.email
            profile = getattr(user, 'userprofile', None)
            if user.profile:
                self.fields['phone'].initial = user.profile.phone
                self.fields['street'].initial = user.profile.street
                self.fields['city'].initial = user.profile.city
                self.fields['zip_code'].initial = user.profile.zip_code
                self.fields['company'].initial = 'None'

    def save(self, user: User) -> Tuple[User,UserProfile]:
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.save()

        profile, created = UserProfile.objects.get_or_create(user=user)

        profile.first_name = self.cleaned_data.get('firstname', '')
        profile.last_name = self.cleaned_data.get('lastname', '')
        profile.email = self.cleaned_data.get('email', '')
        profile.phone = self.cleaned_data.get('phone', '')
        profile.street = self.cleaned_data.get('street', '')
        profile.city = self.cleaned_data.get('city', '')
        profile.zip_code = self.cleaned_data.get('zip_code', '')
        profile.save()

        company_name = self.cleaned_data.get('company', '')

        return user,profile