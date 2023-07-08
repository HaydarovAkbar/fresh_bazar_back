from datetime import datetime

from rest_framework import serializers
from api.models.news import News, Banner


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def destroy(self, instance):
        instance.state_id = 2
        instance.save()
        return instance

    def to_representation(self, instance):
        if instance.state_id == 2:
            return {}
        else:
            return {
                'id': instance.id,
                'title': instance.title,
                'description': instance.description,
                'date_of_created': instance.date_of_created,
                'updated_at': instance.updated_at,
                'image_url': instance.get_image_url,
                'state_name': instance.state.name,
                'state': instance.state.id,
            }


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

    def destroy(self, instance):
        instance.state_id = 2
        instance.save()
        return instance

    def to_representation(self, instance):
        if instance.state_id == 2:
            return {}
        else:
            return {
                'id': instance.id,
                'title': instance.title,
                'description': instance.description,
                'date_of_created': instance.date_of_created,
                'updated_at': instance.updated_at,
                'image_url': instance.get_image_url,
                'state_name': instance.state.name,
                'state': instance.state.id,
            }