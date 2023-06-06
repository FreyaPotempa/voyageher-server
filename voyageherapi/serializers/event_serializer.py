from rest_framework import serializers
from voyageherapi.models import Event, Guide


# class EventGuideSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guide
#         fields = ('first_name', 'last_name', 'username')


class EventSerializer(serializers.ModelSerializer):
    # host = EventGuideSerializer()

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'img_url', 'date_time',
                  'duration', 'available_spots', 'host', 'location_id', 'attendees', 'joined')
        depth = 2
