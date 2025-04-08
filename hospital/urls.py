from django.urls import path
from .views import PatientListCreateAPIView, PatientDetailAPIView
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse(
        "Welcome to Hospital Management API")),
    path('patients/', PatientListCreateAPIView.as_view(),
         name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailAPIView.as_view(),
         name='patient-detail'),
]
