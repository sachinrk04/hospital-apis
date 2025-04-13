from rest_framework import serializers  # type: ignore
from .models import AccountUser


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ['id', 'username', 'email',
                  'password', 'createdAt', 'updatedAt']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AccountUser.objects.create_user(**validated_data)
        return user
