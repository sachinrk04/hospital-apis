from rest_framework import generics  # type: ignore
from .models import AuthUsers
from .serializers import AuthUserSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = AuthUsers.objects.all()
    serializer_class = AuthUserSerializer


class LoginUser(generics.CreateAPIView):
    queryset = AuthUsers.objects.all()
    serializer_class = AuthUserSerializer


class LogoutUser(generics.DestroyAPIView):
    queryset = AuthUsers.objects.all()
    serializer_class = AuthUserSerializer
