from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
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
def upload_success(request):
    return render(
        request,
        'user/upload_profile_photos_success.html',
        {'message': 'Files uploaded successfully!'}
    )