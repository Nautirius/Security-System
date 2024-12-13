from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('all', views.list_users, name='list_users'),
    path('by-id/<int:pk>/', views.user_by_id, name='get_user_by_id'),
    path('create_user/', views.create_user, name='create_user_by_admin'),
    path('edit/<int:pk>/', views.edit_user, name='edit_user_by_Admin'),
    path('delete/<int:pk>/', views.delete_user, name='delete_user_by_admin'),
]