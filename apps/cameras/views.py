from django.shortcuts import render, get_object_or_404, redirect
from .models import Camera
from ..authentication.guards.user_membership_role import user_membership_role
from ..buildings.models import Zone
from django.conf import settings
from django.contrib.auth.decorators import login_required  # TODO: login requirement for CRUD views
from django.http import HttpRequest, HttpResponse


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
