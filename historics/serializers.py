from rest_framework import serializers
from historics.models import Historic


class HistoricSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='location.city')
    date = serializers.DateTimeField(format="%d/%m/%Y", source='created_at')
    class Meta:
        model = Historic
        fields = ['user', 'city', 'date']