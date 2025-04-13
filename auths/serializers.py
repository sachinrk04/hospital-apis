from rest_framework import serializers  # type: ignore
from .models import AuthUsers


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUsers
        fields = '__all__'
