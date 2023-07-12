from rest_framework import serializers
from ...models import info


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.State
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = info.Country
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().update(instance, validated_data)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'shortname': instance.shortname,
            'fullname': instance.fullname,
            'code': instance.code,
            'postal_code': instance.postal_code,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
        }


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.District
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().update(instance, validated_data)
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'shortname': instance.shortname,
            'fullname': instance.fullname,
            'code': instance.code,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
            'region': instance.region.id,
            'region_name': instance.region.shortname,
        }


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.Region
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().update(instance, validated_data)
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'shortname': instance.shortname,
            'fullname': instance.fullname,
            'code': instance.code,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
            'country': instance.country.id,
            'country_name': instance.country.shortname,
        }


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.Language
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.PaymentType
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     validated_data['state_id'] = self.context['request'].data.get('state')
    #     return super().update(instance, validated_data)
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
        }


class UnitOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.UnitOfMeasure
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'abbreviation': instance.abbreviation,
            'date_of_created': instance.date_of_created,
            'state': instance.state.id,
            'state_name': instance.state.name,
        }
