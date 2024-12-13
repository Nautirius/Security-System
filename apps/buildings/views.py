from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Building, Zone
from django.conf import settings
from django.contrib.auth.decorators import login_required  # TODO: login requirement for CRUD views


def home(request):
    return render(request, 'buildings/home.html')


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'buildings/company/company_list.html', {'companies': companies})


def company_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            company = Company(name=name)
            company.save()
        return redirect('company_list')
    else:
        return render(request, 'buildings/company/company_create.html')


def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            company.name = name
            company.save()
        return redirect('company_list')  # TODO: bad request handling
    else:
        return render(request, 'buildings/company/company_update.html', {'company_id': pk, 'old_company': company})


def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if company:
        company.delete()
    return redirect('company_list')


def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'buildings/building/building_list.html', {'buildings': buildings})


def building_create(request):
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


def building_update(request, pk):
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


def building_delete(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if building:
        building.delete()
    return redirect('building_list')


def zone_list(request):
    zones = Zone.objects.all()
    return render(request, 'buildings/zone/zone_list.html', {'zones': zones})


def zone_create(request):
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


def zone_update(request, pk):
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


def zone_delete(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    if zone:
        zone.delete()
    return redirect('zone_list')
