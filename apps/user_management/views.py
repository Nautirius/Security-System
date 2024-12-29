import logging

from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.authentication.models import UserProfile
from apps.user_management.forms import CreateUserManagementForm, UpdateUserManagementForm


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_management/home.html')

@login_required
def list_users(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(
        request,
        'user_management/list_users.html',
        {'users': users}
    )

@login_required
def create_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CreateUserManagementForm(request.POST)
        try:
            if form.is_valid():
                form.save(request)
                return redirect('list_users')

            return render(
                request,
                'user_management/create_user.html',
                {'form': form}
            )
        except Exception as e:
            logging.error(e)
            return render(request, 'user_management/create_user.html', {'form': form})
    else:
        return render(request, 'user_management/create_user.html')

@login_required
def edit_user(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UpdateUserManagementForm(request.POST, user=user)
        if form.is_valid():
            form.save(user)
            return redirect('list_users')

        return render(
            request,
            'user_management/update_user.html',
            {'form': form}
        )
    else:
        form = UpdateUserManagementForm(user=user)
        return render(request, 'user_management/update_user.html', {'form': form, 'user_id': pk})

@login_required
def delete_user(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(User, pk=pk)
    if user:
        user.delete()
    return redirect('list_users')

@login_required
def user_by_id(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(User, pk=pk)
    if user:
        return render(
            request,
            'user_management/user_details.html',
            { user: user }
        )
    return redirect('list_users')