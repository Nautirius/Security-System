from django.urls import path
from . import views

urlpatterns = [
    path('', views.permission_home, name="home_permission"),
    path('create-permission/', views.permission_create,
         name="create_permission"),
    path('list-permissions/', views.permission_list,
         name="list_permissions"),
    path('update-permission/<str:pk>/', views.permission_update,
         name="update_permission"),
    path('delete-permission/<str:pk>/', views.permission_delete,
         name="delete_permission"),
    path('list-users/', views.permission_list_users,
         name='list_users_permissions'),
    path('list-zones/', views.permission_list_zones,
         name='list_zones_permissions'),
    path('update-user-permissions/<str:pk>/', views.permission_user_update,
         name="update_user_permissions"),
    path('update-zone-permissions/<str:pk>/', views.permission_zone_update,
         name="update_zone_permissions"),
]