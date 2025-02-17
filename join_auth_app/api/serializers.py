from rest_framework import serializers
from join_auth_app.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        validated_data['password'] = make_password(validated_data['password'])

        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        token=Token.objects.get_or_create(user=user)
        return user

class UserListSerializer(RegisterSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'date_joined', 'last_login']

class UserDetailSerializer(UserListSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ['id', 'username', 'email', 'password', 'date_joined', 'last_login']