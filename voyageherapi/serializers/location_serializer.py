from rest_framework import serializers
from voyageherapi.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'city')
