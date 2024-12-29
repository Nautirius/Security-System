from django.shortcuts import render, get_object_or_404, redirect
from .models import Camera, CameraFeed
from ..buildings.models import Company, Building, Zone
from ..authentication.guards.user_membership_role import user_membership_role
from django.conf import settings
from django.contrib.auth.decorators import login_required  # TODO: login requirement for CRUD views
from django.http import HttpRequest, HttpResponse
from django.core.files.base import ContentFile
import os


def camera_home(request: HttpRequest) -> HttpResponse:
    return render(request, 'cameras/home.html')


def camera_list(request):
    cameras = Camera.objects.all()
    return render(request, 'cameras/camera_list.html', {'cameras': cameras})


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def camera_create(request):
    if request.method == 'POST':
        label = request.POST['label']
        zone_id = request.POST['zone_id']
        zone = Zone.objects.get(pk=zone_id)
        coordinate_x = request.POST['coordinate_x']
        coordinate_y = request.POST['coordinate_y']
        if label and zone and coordinate_x and coordinate_y:  # TODO: bad request handling
            camera = Camera(label=label, zone=zone, coordinate_x=coordinate_x, coordinate_y=coordinate_y)
            camera.save()
        return redirect('camera_list')
    else:
        zones = Zone.objects.all()
        return render(request, 'cameras/camera_create.html', {'zones': zones})

@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def camera_update(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    if request.method == 'POST':
        label = request.POST['label']
        zone_id = request.POST['zone_id']
        zone = Zone.objects.get(pk=zone_id)
        coordinate_x = request.POST['coordinate_x']
        coordinate_y = request.POST['coordinate_y']
        if label and zone and coordinate_x and coordinate_y:
            camera.label = label
            camera.zone_id = zone
            camera.coordinate_x = coordinate_x
            camera.coordinate_y = coordinate_y
            camera.save()
        return redirect('camera_list')
    else:
        zones = Zone.objects.all()
        return render(request, 'cameras/camera_update.html', {'camera_id': pk, 'old_camera': camera, 'zones': zones})


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def camera_delete(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    if camera:
        camera.delete()
    return redirect('camera_list')


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def camera_feed_grid(request):
    companies = Company.objects.all()
    buildings = Building.objects.all()
    zones = Zone.objects.all()

    selected_company_id = request.GET.get('company')
    selected_building_id = request.GET.get('building')
    selected_zone_id = request.GET.get('zone')

    cameras = Camera.objects.prefetch_related('feeds')
    if selected_company_id:
        cameras = cameras.filter(zone__building__company_id=selected_company_id)
    if selected_building_id:
        cameras = cameras.filter(zone__building_id=selected_building_id)
    if selected_zone_id:
        cameras = cameras.filter(zone_id=selected_zone_id)

    context = {
        'cameras': cameras,
        'companies': companies,
        'buildings': buildings,
        'zones': zones,
        'selected_company_id': selected_company_id,
        'selected_building_id': selected_building_id,
        'selected_zone_id': selected_zone_id,
    }
    return render(request, 'cameras/camera_feed_grid.html', context)


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def camera_feed_upload(request):
    if request.method == 'POST':
        camera_id = request.POST['camera']
        image_path = request.FILES['image_path']
        camera = get_object_or_404(Camera, pk=camera_id)

        feed, created = CameraFeed.objects.get_or_create(camera=camera)

        if feed.image_path_face:
            feed.image_path_face.delete(save=False)
        if feed.image_path_silhouette:
            feed.image_path_silhouette.delete(save=False)

        feed.image_path_face.save(f"{camera.label}_face.jpg", ContentFile(image_path.read()))
        image_path.seek(0)
        feed.image_path_silhouette.save(f"{camera.label}_silhouette.jpg", ContentFile(image_path.read()))
        feed.save()

        return redirect('camera_feed_grid')
    else:
        cameras = Camera.objects.all()
        return render(request, 'cameras/camera_feed_upload.html', {'cameras': cameras})

