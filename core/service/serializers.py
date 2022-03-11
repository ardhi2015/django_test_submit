from rest_framework import serializers

from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    email = serializers.CharField()
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        exclude = (
            "groups",
            "is_active",
            "is_superuser",
            "last_login",
            "user_permissions",
        )


class UserResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    result = UserSerializer()
