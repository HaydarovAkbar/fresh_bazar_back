from rest_framework import serializers
from api.models import category


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.ProductCategory
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'state_name': instance.state.name,
            'state': instance.state.id,
            'date_of_created': instance.date_of_created,
            'updated_at': instance.updated_at,
            'image': instance.get_image_url,
        }

