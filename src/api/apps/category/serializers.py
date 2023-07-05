from rest_framework import serializers
from ...models import category


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.ProductCategory
        fields = '__all__'

    def create(self, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'state': instance.state.name,
            'state_id': instance.state.id,
            'date_of_created': instance.date_of_created,
            'updated_at': instance.updated_at,
        }
