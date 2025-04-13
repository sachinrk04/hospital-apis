from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from django.http import HttpResponse  # type: ignore

urlpatterns = [
    path("", lambda request: HttpResponse(
        "<h1>Welcome to Hospital Management API</h1>")),
    path("admin/", admin.site.urls),
    path("hospital/", include("hospital.urls")),
]
