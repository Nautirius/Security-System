from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.company_create, name='company_create'),
    path('companies/<int:pk>/update/', views.company_update, name='company_update'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),

    path('buildings/', views.building_list, name='building_list'),
    path('buildings/create/', views.building_create, name='building_create'),
    path('buildings/<int:pk>/update/', views.building_update, name='building_update'),
    path('buildings/<int:pk>/delete/', views.building_delete, name='building_delete'),

    path('zones/', views.zone_list, name='zone_list'),
    path('zones/create/', views.zone_create, name='zone_create'),
    path('zones/<int:pk>/update/', views.zone_update, name='zone_update'),
    path('zones/<int:pk>/delete/', views.zone_delete, name='zone_delete'),
]
