from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, permission_classes
from django.contrib.auth.models import User
from voyageherapi.models import Traveler, Guide, Rating
from voyageherapi.serializers import UserSerializer, GuideSerializer


class GuideView(ViewSet):

    def list(self, request):
        '''list of all users'''
        guides = Guide.objects.all().prefetch_related('ratings')
        serializer = GuideSerializer(guides, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            guide = Guide.objects.get(pk=pk)
            serializer = GuideSerializer(guide)
            return Response(serializer.data)
        except Guide.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=True, url_path='rate-guide')
    def rate_guide(self, request, pk):
        '''rate a guide'''
        guide = Guide.objects.get(pk=pk)
        user = request.auth.user
        traveler = user.traveler

        try:
            rating = Rating.objects.get(
                traveler=traveler, guide=guide)
            rating.score = request.data['score']
            rating.review = request.data['review']
            rating.save()
        except Rating.DoesNotExist:
            rating = Rating.objects.create(
                traveler=traveler, guide=guide, score=request.data['score'], review=request.data['review'])

        return Response({'message': "Rating added"}, status=status.HTTP_201_CREATED)
