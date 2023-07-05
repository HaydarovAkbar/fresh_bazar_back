from rest_framework import serializers
from ...models import discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = discount.Discount
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'description': instance.description,
            'discount_percent' : instance.discount_percent,
            'date_of_created': instance.date_of_created,
            'updated_at': instance.updated_at,
            'state': instance.state.name,
            'state_id': instance.state.id,
        }