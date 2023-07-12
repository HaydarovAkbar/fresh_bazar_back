from rest_framework import serializers
from api.models import suppliers


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = suppliers.Suppliers
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'brand': instance.brand,
            'state_name': instance.state.name,
            'state': instance.state.id,
            'date_of_created': instance.date_of_created,
            'image': instance.get_image_url,
            'weight': instance.weight,
            'price': instance.price,
            'supply_date': instance.supply_date,
            'bar_code': instance.bar_code,
            'certificate': instance.get_certificate_url,
            'market_share': instance.market_share,
            'applied': instance.applied,
            'partnership': instance.partnership,
            'unit_of_measure': instance.unit_of_measure.id,
            'unit_of_measure_name': instance.unit_of_measure.name,
        }