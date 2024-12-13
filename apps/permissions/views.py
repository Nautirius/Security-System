from django.shortcuts import render, redirect
from .models import Permission
from .forms import PermissionForm

# Create your views here.
def permission_home(request):
    context = {}
    return render(request,  "permissions/permission_home.html",
                  context)

def permission_list(request):
    permissions = Permission.objects.all()
    context = {'permissions': permissions }
    return render(request, 'permissions/permission_list.html',
                  context)

def permission_create(request):
    form = PermissionForm()
    context = {'form': form}
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('permission_home')
    return render(request, "permissions/permission_create.html",
                  context)

def permission_update(request, pk):
    permission = Permission.objects.get(id=pk)
    form = PermissionForm(instance=permission)
    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=permission)
        if form.is_valid():
            form.save()
            return redirect('permission_home')
    context = {'form': form}
    return render(request, "permissions/permission_create.html",
                  context)

def permission_delete(request, pk):
    permission = Permission.objects.get(id=pk)
    if request.method == 'POST':
        permission.delete()
        return redirect('permission_home')
    context = {'permission': permission}
    return render(request, "permissions/permission_delete.html",
                  context)