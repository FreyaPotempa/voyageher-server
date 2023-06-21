from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from voyageherapi.models import Guide, Traveler, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    '''serializer for users'''
    user_type = serializers.SerializerMethodField()
    traveler = serializers.SerializerMethodField()
    guide = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'user_type', 'traveler', 'guide']

    def get_user_type(self, obj):
        if hasattr(obj, 'traveler'):
            return 'traveler'
        elif hasattr(obj, 'guide'):
            return 'guide'
        else:
            return 'unknown'

    def get_traveler(self, obj):
        if hasattr(obj, 'traveler'):
            serializer = TravelerSerializer(obj.traveler)
            return serializer.data
        else:
            return None

    def get_guide(self, obj):
        if hasattr(obj, 'guide'):
            serializer = GuideSerializer(obj.guide)
            return serializer.data
        else:
            return None


class GuideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guide
        fields = ['id', 'location',
                  'bio', 'img', 'user_id', 'full_name', 'average_rating', 'ratings']
        depth = 1


class TravelerSerializer(serializers.ModelSerializer):
    '''serializer for travelers'''
    class Meta:
        model = Traveler
        fields = ['bio', 'user_id']
        depth = 2


class AddGuideRatingSerializer(serializers.Serializer):
    score = serializers.IntegerField()
    rating = serializers.CharField()
