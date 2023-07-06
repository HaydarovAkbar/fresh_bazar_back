from datetime import datetime

from rest_framework import serializers
from api.models.product import Product, ProductInventory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().update(instance, validated_data)

    def destroy(self, instance):
        instance.state_id = 2
        instance.deleted_at = datetime.now()
        instance.save()
        return instance

    def to_representation(self, instance):
        if instance.state_id == 2:
            return {}
        else:
            return {
                'id': instance.id,
                'uuid': instance.uuid,
                'name': instance.name,
                'description': instance.description,
                'price': instance.price,
                'sku': instance.sku,
                'date_of_created': instance.date_of_created,
                'updated_at': instance.updated_at,
                'image_url': instance.get_image_url,
                'product_category': instance.product_category.name,
                'product_inventory': instance.product_inventory.quantity,
                'discount': instance.discount,
                'state': instance.state.name,
                'state_id': instance.state.id,
                'product_category_id': instance.product_category.id,
                'product_inventory_id': instance.product_inventory.id,
            }


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'quantity': instance.quantity,
            'date_of_created': instance.date_of_created,
            'updated_at': instance.updated_at,
            'deleted_at': instance.deleted_at,
        }
