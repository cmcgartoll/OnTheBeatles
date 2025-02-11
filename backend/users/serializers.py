from rest_framework import serializers
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',
                'first_name', 
                'last_name', 
                'username', 
                'email', 
                'password', 
                'phone',
                'date_joined',
                'is_active',
                'is_staff']
        read_only_field = ['date_joined', 'is_active', 'is_staff']

class SignUpSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = CustomUser
        fields = ['id',
                'first_name', 
                'last_name', 
                'username', 
                'email', 
                'password', 
                'phone',
                'date_joined',
                'is_active',
                'is_staff']
    
    def create(self, validated_data):
        try:
            user = CustomUser.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class TokenSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source='Authorization')
    class Meta:
        model = Token 
        fields = ['key']
