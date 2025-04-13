from rest_framework import generics  # type: ignore
from rest_framework.exceptions import ValidationError  # type: ignore
from rest_framework.response import Response  # type: ignore
from datetime import datetime
from .models import Patient
from .serializers import PatientSerializer


class PatientListCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        # Validate first name and last name length
        firstName = request.data.get('firstName', '')
        if len(firstName) < 3:
            raise ValidationError(
                "First name must be at least 3 characters")
        # Validate last name length
        lastName = request.data.get('lastName', '')
        if len(lastName) < 2:
            raise ValidationError(
                "Last name must be at least 2 characters")

        # Validate phone number format
        phone = request.data.get('phone', '')
        if not phone.isdigit() or len(phone) < 10 or len(phone) > 15:
            raise ValidationError("Phone number must be between 10-15 digits")

        # Validate date of birth
        try:
            dob = request.data.get('dob')
            if dob is None:
                raise ValidationError("Date of birth is required")
            dob = datetime.strptime(dob, '%Y-%m-%d')
            if dob > datetime.now():
                raise ValidationError("Date of birth cannot be in the future")
        except ValueError:
            raise ValidationError("Invalid date format. Use YYYY-MM-DD")
        address = request.data.get('address', '')
        if len(address) < 10:
            raise ValidationError("Address must be at least 10 characters")

        response = super().create(request, *args, **kwargs)
        return response


class PatientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return response


class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [{'id': patient['id'],
                 'firstName': patient['firstName'],
                 'lastName': patient['lastName'],
                 'dob': patient['dob'],
                 'phone': patient['phone']}
                for patient in serializer.data]
        return Response(data)


class PatientUpdateAPIView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        response = super().update(request, *args, **kwargs)
        return response


class PatientDeleteAPIView(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Patient deleted successfully"})
