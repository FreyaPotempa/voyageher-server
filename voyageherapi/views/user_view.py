from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from voyageherapi.models import Traveler, Guide
from voyageherapi.serializers import UserSerializer, GuideSerializer


class UserView(ViewSet):

    def list(self, request):
        '''list of all users'''
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):

        try:
            user = User.objects.get(pk=pk)

            if hasattr(user, 'traveler'):
                traveler = user.traveler
                traveler.bio = request.data.get('traveler').get('bio')
                traveler.img = request.data.get('traveler').get('img')
                traveler.save()
            elif hasattr(user, 'guide'):
                guide = user.guide
                guide.bio = request.data.get('guide').get('bio')
                guide.img = request.data.get('guide').get('img')
                guide.save()
            else:
                return Response({'message': "user cannot but updated"})

            return Response({'message': 'user updated successfully'})

        except User.DoesNotExist:

            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
