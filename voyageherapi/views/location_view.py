from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from voyageherapi.models import Event, Guide, Location, Traveler
from voyageherapi.serializers import LocationSerializer


class LocationView(ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        '''returns a list of all locations'''
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        '''get a single location'''
        try:
            location = Location.objects.get(pk=pk)
            serializer = LocationSerializer(location)
            return Response(serializer.data)
        except Location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        '''handles POST locations'''

        location = Location.objects.create(city=request.data['city'])

        serializer = LocationSerializer(location)
        return Response(serializer.data)
