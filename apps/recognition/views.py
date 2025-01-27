from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from pgvector.django.functions import L2Distance

from apps.authentication.models import UserImage
from apps.recognition.feature_extraction.face_feature_extarction_model import FaceFeatureExtractionModel
from apps.recognition.feature_extraction.pose_feature_extraction_model import PoseFeatureExtractionModel


@csrf_exempt
def verify_user_by_image(request):
    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            image_type = request.POST.get('image_type')  # 'face' lub 'silhouette'

            if not image or not image_type:
                return JsonResponse({'message': 'Invalid request. Missing image or image_type.'}, status=400)

            model = FaceFeatureExtractionModel() if image_type == 'face' else PoseFeatureExtractionModel()
            embedding = model.extract_features(image)

            closest_image = (
                UserImage.objects.filter(image_type=image_type)
                .annotate(distance=L2Distance(F('embedding'), embedding))
                .order_by('distance')
                .first()
            )

            THRESHOLD = 0.5
            if closest_image and closest_image.distance < THRESHOLD:
                user = closest_image.user
                return JsonResponse({
                    'message': 'User found',
                    'user': {
                        'id': user.id,
                        'name': f"{user.profile.first_name} {user.profile.last_name}",
                        'email': user.profile.email
                    }
                })
            else:
                return JsonResponse({'message': 'No matching user found.'}, status=404)
        except Exception as e:
            return JsonResponse({'message': 'Error processing the request.', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method. Use POST.'}, status=405)


@csrf_exempt
def verify_user_data_and_image(request):
    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            image_type = request.POST.get('image_type')  # 'face' lub 'silhouette'
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            if not image or not image_type or not first_name or not last_name or not email:
                return JsonResponse({'message': 'Invalid request. Missing required fields.'}, status=400)

            model = FaceFeatureExtractionModel() if image_type == 'face' else PoseFeatureExtractionModel()
            embedding = model.extract_features(image)

            try:
                user = User.objects.get(profile__first_name=first_name, profile__last_name=last_name, profile__email=email)
            except User.DoesNotExist:
                return JsonResponse({'message': 'No user found with the given data.'}, status=404)

            closest_image = (
                UserImage.objects.filter(user=user, image_type=image_type)
                .annotate(distance=L2Distance(F('embedding'), embedding))
                .order_by('distance')
                .first()
            )

            THRESHOLD = 0.5
            if closest_image and closest_image.distance < THRESHOLD:
                return JsonResponse({'message': 'Image and user data match.'})
            else:
                return JsonResponse({'message': 'Image does not match the given user data.'}, status=404)
        except Exception as e:
            return JsonResponse({'message': 'Error processing the request.', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method. Use POST.'}, status=405)