from rest_framework import generics  # type: ignore
from rest_framework.permissions import AllowAny  # type: ignore
from .models import AccountUser
from .serializers import AccountUserSerializer


class AccountUserRegisterView(generics.CreateAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
    permission_classes = [AllowAny]


class AccountUserLoginView(generics.CreateAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer


class AccountUserLogoutView(generics.DestroyAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
