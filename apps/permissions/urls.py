from django.urls import path
from . import views

urlpatterns = [
    path('', views.permission_home, name="home_permission"),
    path('create_permission/', views.permission_create,
         name="create_permission"),
    path('list_permissions/', views.permission_list,
         name="list_permissions"),
    path('update_permission/<str:pk>/', views.permission_update,
         name="update_permission"),
    path('delete_permission/<str:pk>/', views.permission_delete,
         name="delete_permission"),
    path('list_users/', views.permission_list_users,
         name='list_users_permissions'),
    path('list_zones/', views.permission_list_zones,
         name='list_zones_permissions'),
    path('update_user_permissions/<str:pk>/', views.permission_user_update,
         name="update_user_permissions"),
    path('update_zone_permissions/<str:pk>/', views.permission_zone_update,
         name="update_zone_permissions"),
]