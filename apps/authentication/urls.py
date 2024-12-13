from django.urls import path, include
from . import views


urlpatterns = [
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/", include("allauth.urls")),
    path('upload/', views.upload_images, name='upload_images'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('uploaded-photos-list/', views.uploaded_profile_photos, name='uploaded'),

    path('user-photo/<str:folder_name>/<str:photo_type>/<str:name>/', views.user_photo, name='user-photo'),
]