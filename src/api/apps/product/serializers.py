from datetime import datetime

from rest_framework import serializers
from api.models.product import Product, ProductInventory, TopProduct


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
                'product_category_name': instance.product_category.name,
                'product_inventory_name': instance.product_inventory.quantity,
                'discount': instance.discount,
                'state_name': instance.state.name,
                'state': instance.state.id,
                'product_category': instance.product_category.id,
                'product_inventory': instance.product_inventory.id,
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


class TopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProduct
        fields = '__all__'

    def to_representation(self, instance):
        if instance.state_id == 2:
            return {}
        return {
            'id': instance.id,
            'product_name': instance.product.name,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
            'product': instance.product.id,
            'image_url': instance.product.get_image_url,
            'price': instance.product.price,
            'discount': instance.product.discount.id,
            'discount_name': instance.product.discount.name,
            'discount_value': instance.product.discount.value,
        }