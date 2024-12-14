from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Building, Zone
from django.conf import settings
from django.contrib.auth.decorators import login_required  # TODO: login requirement for CRUD views
from django.contrib import messages

from ..authentication.models import Membership


def home(request):
    return render(request, 'buildings/home.html')

def company_home(request: HttpRequest) -> HttpResponse:
    return render(request, 'buildings/company/home.html')

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'buildings/company/company_list.html', {'companies': companies})


def company_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            company = Company(name=name)
            company.save()
        return redirect('company_list')
    else:
        return render(request, 'buildings/company/company_create.html')


def assign_user_to_company(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            company_id = request.POST['company_id']
            role = request.POST['role']

            if user_id and company_id:
                user = get_object_or_404(User, id=user_id)
                company = get_object_or_404(Company, id=company_id)

                user_profile = user.profile

                membership_exists = Membership.objects.filter(
                    user_profile=user_profile,
                    company=company
                ).exists()

                if membership_exists:
                    messages.error(request, f"Użytkownik {user.username} jest już przypisany do firmy {company.name}.")
                else:
                    Membership.objects.create(
                        user_profile=user_profile,
                        company=company,
                        role=role
                    )
                    messages.success(request, f"Użytkownik {user.username} został przypisany do firmy {company.name} jako {role}.")
            else:
                messages.error(request, "Musisz wybrać użytkownika i firmę.")

            return redirect('assign_user_to_company')

        except Exception as e:
            return redirect('assign_user_to_company')

    users = User.objects.all()
    companies = Company.objects.all()

    return render(
        request,
        'buildings/company/assign_user_to_company.html',
        { "users": users, "companies": companies }
    )

def company_update(request: HttpRequest, pk) -> HttpResponse:
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            company.name = name
            company.save()
        return redirect('company_list')  # TODO: bad request handling
    else:
        return render(request, 'buildings/company/company_update.html', {'company_id': pk, 'old_company': company})


def company_delete(request: HttpRequest, pk: int) -> HttpResponse:
    company = get_object_or_404(Company, pk=pk)
    if company:
        company.delete()
    return redirect('company_list')


def buildings_home(request: HttpRequest) -> HttpResponse:
    return render(request, 'buildings/building/home.html')


def building_list(request: HttpRequest) -> HttpResponse:
    buildings = Building.objects.all()
    return render(request, 'buildings/building/building_list.html', {'buildings': buildings})


def building_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        label = request.POST['label']
        company_id = request.POST['company_id']
        company = Company.objects.get(pk=company_id)
        if label and company:
            building = Building(label=label, company=company)
            building.save()
        return redirect('building_list')
    else:
        companies = Company.objects.all()
        return render(request, 'buildings/building/building_create.html', {'companies': companies})


def building_update(request: HttpRequest, pk: int) -> HttpResponse:
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        label = request.POST['label']
        company_id = request.POST['company_id']
        company = Company.objects.get(pk=company_id)
        if label and company:
            building.label = label
            building.company = company
            building.save()
        return redirect('building_list')
    else:
        companies = Company.objects.all()
        return render(request, 'buildings/building/building_update.html', {'building_id': pk, 'old_building': building,
                                                                           'companies': companies})


def building_delete(request: HttpRequest, pk: int) -> HttpResponse:
    building = get_object_or_404(Building, pk=pk)
    if building:
        building.delete()
    return redirect('building_list')


def zone_home(request: HttpRequest) -> HttpResponse:
    return render(request, 'buildings/zone/home.html')

def zone_list(request: HttpRequest) -> HttpResponse:
    zones = Zone.objects.all()
    return render(request, 'buildings/zone/zone_list.html', {'zones': zones})


def zone_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        label = request.POST['label']
        building_id = request.POST['building_id']
        building = Building.objects.get(pk=building_id)
        if label and building:
            zone = Zone(label=label, building=building)
            zone.save()
        return redirect('zone_list')
    else:
        buildings = Building.objects.all()
        return render(request, 'buildings/zone/zone_create.html', {'buildings': buildings})


def zone_update(request: HttpRequest, pk: int) -> HttpResponse:
    zone = get_object_or_404(Zone, pk=pk)
    if request.method == 'POST':
        label = request.POST['label']
        building_id = request.POST['building_id']
        building = Building.objects.get(pk=building_id)
        if label and building:
            zone.label = label
            zone.building = building
            zone.save()
        return redirect('zone_list')
    else:
        buildings = Building.objects.all()
        return render(request, 'buildings/zone/zone_update.html', {'zone_id': pk, 'old_zone': zone,
                                                                   'buildings': buildings})


def zone_delete(request: HttpRequest, pk: int) -> HttpResponse:
    zone = get_object_or_404(Zone, pk=pk)
    if zone:
        zone.delete()
    return redirect('zone_list')
