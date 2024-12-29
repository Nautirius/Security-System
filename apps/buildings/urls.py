from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/home/', views.company_home, name='company_home'),
    path('companies/create/', views.company_create, name='company_create'),
    path('companies/<int:pk>/update/', views.company_update, name='company_update'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),
    path('companies/assign_user_to_company/', views.assign_user_to_company, name='assign_user_to_company'),
    path('companies/by-id/<int:pk>/', views.company_by_id, name='company_by_id'),
    path('companies/fire-user/<int:company_id>/<int:user_id>/', views.company_fire_user, name='fire_user_from_company'),
    path('companies/promote-user/<int:company_id>/<int:user_id>/', views.company_promote_user, name='promote_user_at_company'),
    path('companies/degrade-user/<int:company_id>/<int:user_id>/', views.company_degrade_user, name='degrade_user_at_company'),

    path('buildings/', views.building_list, name='building_list'),
    path('buildings/home/', views.buildings_home, name='building_home'),
    path('buildings/create/', views.building_create, name='building_create'),
    path('buildings/<int:pk>/update/', views.building_update, name='building_update'),
    path('buildings/<int:pk>/delete/', views.building_delete, name='building_delete'),

    path('zones/', views.zone_list, name='zone_list'),
    path('zones/home/', views.zone_home, name='zone_home'),
    path('zones/create/', views.zone_create, name='zone_create'),
    path('zones/<int:pk>/update/', views.zone_update, name='zone_update'),
    path('zones/<int:pk>/delete/', views.zone_delete, name='zone_delete'),
]
