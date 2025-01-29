from django.urls import path
from . import views

urlpatterns = [
    path('verify-user-by-image/', views.verify_user_by_image, name='verify_user_by_image'),
    path('verify-user-data-and-image/', views.verify_user_data_and_image, name='verify_user_data_and_image'),
]
