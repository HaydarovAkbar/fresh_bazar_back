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

    def create(self, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().update(instance, validated_data)
