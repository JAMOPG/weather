from rest_framework import serializers
from historics.models import Historic


class HistoricSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='locations.city')
    class Meta:
        model = Historic
        fields = ['user', 'created_at', 'city']