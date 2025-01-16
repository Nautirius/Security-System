import logging
import os
from pprint import pformat

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
                # model = PoseFeatureExtractionModel(path)
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


@login_required
def uploaded_profile_photos(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        return redirect('/dashboard')

    user = request.user
    face_images = user.images.filter(image_type='face')
    silhouette_images = user.images.filter(image_type='silhouette')

    return render(request, 'user/user_uploaded_photos.html', {
        'face_images': face_images,
        'silhouette_images': silhouette_images
    })

@api_view(['GET'])
def user_photo(request,  folder_name: str, photo_type: str, name: str):
    if not request.user.is_authenticated:
        return Response({"error": "User not authenticated"}, status=403)

    try:
        folder_owner_id = folder_name.split('_')[-1]
        storage = FileStorage()
        # if folder_owner_id != request.user.id:
        #     return Response({"error": "Permission denied"}, status=404)

        # photo = get_object_or_404(UserImage, user=request.user, name=f'{folder_name}/{photo_type}/{name}')
        photo = UserImage.objects.get(file_path=f'{folder_name}/{photo_type}/{name}')
        file_full_path = storage.get_file_path(photo.file_path)

    except UserImage.DoesNotExist:
        return Response({"error": "Photo not found or permission denied"}, status=404)

    if not os.path.exists(file_full_path):
        return Response({"error": "File not found"}, status=404)

    return FileResponse(open(file_full_path, 'rb'), as_attachment=True)