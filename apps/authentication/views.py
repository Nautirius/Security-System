import logging
from pprint import pformat

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import CustomSignupForm
from .models import UserImage
from .storage import FileStorage

@login_required
def upload_images(request):
    if request.method == 'POST':
        storage = FileStorage()
        user = request.user

        for image_type in ['face', 'silhouette']:
            images = request.FILES.getlist(f'{image_type}_images')
            for file in images:
                relative_path = f'user_{user.id}/{image_type}/{file.name}'
                saved_path = storage.save_file(file, relative_path)

                UserImage.objects.create(user=user, image_type=image_type, file_path=relative_path)

        return redirect('/auth/upload/success')

    return render(request, 'user/upload_profile_photos.html')


@login_required
def upload_success(request: HttpRequest):
    return render(
        request,
        'user/upload_profile_photos_success.html',
        {'message': 'Files uploaded successfully!'}
    )


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        try:
            logging.info(request.POST)
            if form.is_valid():
                form.save(request)
                return redirect('/auth/accounts/login')
            else:
                logging.error(f"Form errors: {form.errors}")
                return render(request, 'account/signup.html', {'form': form})

        except Exception as e:
            logging.error("ERROR")
            logging.error(pformat(request))
            logging.error(e)
            logging.error("\n\n" + "="*20+ '\n')
            return render(request, 'account/signup.html', {'form': form})



    form = CustomSignupForm()
    return render(request, 'account/signup.html', {'form': form})