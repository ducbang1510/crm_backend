from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField, DateTimeField
from oauth2_provider.models import Application
from crm.models.user import User

class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name",
                  "username", "password", "email", "is_staff", "is_active", "date_joined"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }