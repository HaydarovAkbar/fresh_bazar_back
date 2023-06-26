from rest_framework import serializers
from ...models import info


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.State
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = info.State
        fields = '__all__'

    def create(self, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().update(instance, validated_data)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.State
        fields = '__all__'

    def create(self, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().update(instance, validated_data)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = info.State
        fields = '__all__'

    def create(self, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['state_id'] = self.context['request'].data.get('state')
        return super().update(instance, validated_data)