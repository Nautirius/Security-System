from allauth.core.internal.httpkit import redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_management/home.html')

def list_users(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(
        request,
        'user_management/list_users.html',
        {'users': users}
    )

def create_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        pass
    else:
        return render(request, 'user_management/create_user.html')

def edit_user(request: HttpRequest, pk) -> HttpResponse:
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'user_management/update_user.html')


def delete_user(request: HttpRequest, pk) -> HttpResponse:
    user = get_object_or_404(User, pk=pk)
    if user:
        user.delete()
    return redirect('list_users')


def user_by_id(request: HttpRequest, pk) -> HttpResponse:
    return redirect('list_users') # TODO: