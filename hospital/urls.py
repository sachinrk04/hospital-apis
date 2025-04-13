from django.urls import path  # type: ignore
from .views import (
    PatientListCreateAPIView,
    PatientDetailAPIView,
    PatientListAPIView,
    PatientUpdateAPIView,
    PatientDeleteAPIView
)
from django.http import HttpResponse  # type: ignore

urlpatterns = [
    path('', lambda request: HttpResponse(
        "Welcome to Hospital Management API")),
    path('patients/', PatientListCreateAPIView.as_view(),
         name='patient-create', kwargs={'get': None}),
    path('patients/<int:pk>/', PatientDetailAPIView.as_view(),
         name='patient-detail'),
    path('patients/list/', PatientListAPIView.as_view(),
         name='patient-list'),
    path('patients/update/<int:pk>/', PatientUpdateAPIView.as_view(),
         name='patient-update'),
    path('patients/delete/<int:pk>/', PatientDeleteAPIView.as_view(),
         name='patient-delete'),
]
