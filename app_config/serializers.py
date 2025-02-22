from rest_framework import serializers
from random import randint

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'password', 'full_name', 'gander', 'birthdate',
                  'is_active', 'is_staff', 'is_admin')

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords must match")

        return data

    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("confirm_password")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone',)

class SMSSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()

class VerifySMSSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    verification_code = serializers.CharField()