from django.shortcuts import render, redirect
from .models import Permission
from apps.authentication.models import UserProfile
from apps.buildings.models import Zone
from .forms import PermissionForm, UserPermissionForm, ZonePermissionForm
from django.contrib.auth.decorators import login_required
from ..authentication.guards.user_membership_role import user_membership_role


def permission_home(request):
    return render(request,  "permissions/permission_home.html")


def permission_list(request):
    permissions = Permission.objects.all()
    context = {'permissions': permissions}
    return render(request, 'permissions/permission_list.html', context)


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def permission_create(request):
    form = PermissionForm(title="Create new Permission")
    context = {'form': form}
    if request.method == 'POST':
        form = PermissionForm(request.POST, title="Create new Permission")
        if form.is_valid():
            form.save()
            return redirect(permission_list)
    return render(request, "permissions/permission_form.html", context)


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def permission_update(request, pk):
    permission = Permission.objects.get(id=pk)
    form = PermissionForm(instance=permission, title="Edit Permission")
    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=permission, title="Edit Permission")

        if form.is_valid():
            form.save()
            return redirect(permission_list)
    context = {'form': form}
    return render(request, "permissions/permission_form.html", context)


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def permission_delete(request, pk):
    permission = Permission.objects.get(id=pk)
    permission.delete()
    return redirect(permission_list)


def permission_list_users(request):
    users = UserProfile.objects.all()
    context = {'users': users}
    return render(request, 'permissions/permission_list_users.html', context)


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def permission_user_update(request, pk):
    user = UserProfile.objects.get(id=pk)
    form = UserPermissionForm(user=user, title="Edit User Permissions")
    if request.method == 'POST':
        form = UserPermissionForm(request.POST, user=user, title="Edit User Permissions")
        if form.is_valid():
            user.permission_set.clear()
            for permission in form.cleaned_data["permissions"]:
                user.permission_set.add(permission)
            return redirect(permission_list_users)
    context = {"form": form}
    return render(request, "permissions/permission_form.html", context)


def permission_list_zones(request):
    zones = Zone.objects.all()
    context = {'zones': zones}
    return render(request, 'permissions/permission_list_zones.html', context)


@login_required
@user_membership_role(roles=['MANAGEMENT', 'ADMIN'])
def permission_zone_update(request, pk):
    zone = Zone.objects.get(id=pk)
    form = ZonePermissionForm(zone=zone, title="Edit Zone Permissions")
    if request.method == 'POST':
        form = ZonePermissionForm(request.POST, zone=zone, title="Edit Zone Permissions")
        if form.is_valid():
            zone.permission_set.clear()
            for permission in form.cleaned_data["permissions"]:
                zone.permission_set.add(permission)
            return redirect(permission_list_zones)
    context = {"form": form}
    return render(request, "permissions/permission_form.html", context)
