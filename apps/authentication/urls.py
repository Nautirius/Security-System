from django.urls import path, include
from . import views


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('upload/', views.upload_images, name='upload_images'),
    path('upload/success/', views.upload_success, name='upload_success'),
]