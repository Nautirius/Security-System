"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path, include, re_path
from django.http import HttpRequest, HttpResponse

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from django.conf import settings
from django.conf.urls.static import static

from core.views import full_text_search_view

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Dokumentacja API dla Security System App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="aswietek@student.agh.edu.pl"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


@login_required
def dashboard_view(request: HttpRequest) -> HttpResponse:
    return render(request, "dashboard.html", {})


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {})


urlpatterns = [

    path("", index_view, name="index"),
    path("admin/", admin.site.urls),
    path("auth/", include("apps.authentication.urls")),

    path("user_management/", include("apps.user_management.urls")),
    path("buildings/", include("apps.buildings.urls")),
    path("permissions/", include("apps.permissions.urls")),

    path("recognition/", include("apps.recognition.urls")),

    path("cameras/", include("apps.cameras.urls")),

    path("dashboard/", dashboard_view, name="dashboard"),

    path("search/", full_text_search_view, name="search"),

    # SWAGGER DOCS
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
