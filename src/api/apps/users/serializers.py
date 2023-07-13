from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    user_permissions = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups',
            'user_permissions',)


class UserSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login',
                  'date_joined', 'groups', 'user_permissions',)
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user


class UserSerializersUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login',
                  'date_joined', 'groups', 'user_permissions',)
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        user = User.objects.get(id=instance.id)
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.is_staff = validated_data.get('is_staff', user.is_staff)
        user.is_active = validated_data.get('is_active', user.is_active)
        user.is_superuser = validated_data.get('is_superuser', user.is_superuser)
        user.last_login = validated_data.get('last_login', user.last_login)
        user.date_joined = validated_data.get('date_joined', user.date_joined)
        user.groups = validated_data.get('groups', user.groups)
        user.user_permissions = validated_data.get('user_permissions', user.user_permissions)
        user.save()
        return user

