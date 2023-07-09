from rest_framework import serializers
from api.models.product import Product, ProductInventory, TopProduct, BestOffer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # def destroy(self, instance):
    #     instance.state_id = 2
    #     instance.deleted_at = datetime.now()
    #     instance.save()
    #     return instance

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
                'discount': instance.discount.id if instance.discount else None,
                'discount_name': instance.discount.name if instance.discount else None,
                'discount_value': instance.discount.value if instance.discount else None,
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
            'discount': instance.product.discount.id if instance.product.discount else None,
            'discount_name': instance.product.discount.name if instance.product.discount else None,
            'discount_value': instance.product.discount.value if instance.product.discount else None,
        }


class BestOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestOffer
        fields = '__all__'

    def to_representation(self, instance):
        if instance.state_id == 2:
            return {}
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
            'image_url': instance.product.get_image_url,
        }