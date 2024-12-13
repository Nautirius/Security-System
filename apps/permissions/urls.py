from django.urls import path
from . import views

urlpatterns = [
    path('', views.permission_home, name="permission_home"),
    path('create-permission/', views.permission_create,
         name="create-permission"),
    path('list-permissions/', views.permission_list,
         name="list-permissions"),
    path('update-permission/<str:pk>/', views.permission_update,
         name="update-permission"),
    path('delete-permission/<str:pk>/', views.permission_delete,
         name="delete-permission"),
]