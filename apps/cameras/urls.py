from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera_list, name='camera_list'),
    path('home/', views.camera_home, name='camera_home'),
    path('create/', views.camera_create, name='camera_create'),
    path('<int:pk>/update/', views.camera_update, name='camera_update'),
    path('<int:pk>/delete/', views.camera_delete, name='camera_delete'),
]
