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
