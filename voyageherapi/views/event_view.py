from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from voyageherapi.models import Event, Guide, Location, Traveler
from voyageherapi.serializers import EventSerializer
from rest_framework.decorators import action


class EventView(ViewSet):

    def list(self, request):
        '''get a list of all events'''
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        '''get a single event'''
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        '''handles POST events'''

        host = Guide.objects.get(user=request.auth.user)
        location_id = Location.objects.get(
            id=request.data['location_id'])

        event = Event.objects.create(title=request.data['title'], description=request.data['description'], img_url=request.data['img_url'],
                                     date_time=request.data['date_time'], duration=request.data["duration"], available_spots=request.data['available_spots'], host=host, location=location_id)

        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        '''handles PUT requests for event'''

        event = Event.objects.get(pk=pk)
        event.title = request.data['title']
        event.description = request.data['description']
        event.img_url = request.data['img_url']
        event.date_time = request.data['date_time']
        event.duration = request.data['duration']
        event.available_spots = request.data['available_spots']
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        '''deletes an event'''
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        '''POST request for traveler to join event'''
        traveler = Traveler.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(traveler)
        return Response({'message': 'Traveler added'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        '''DELETE request for traveler to leave event'''
        traveler = Traveler.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(traveler)
        return Response({'message': 'Traveler removed'}, status=status.HTTP_204_NO_CONTENT)
