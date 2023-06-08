from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from voyageherapi.models import Traveler, Guide
from voyageherapi.serializers import UserSerializer, GuideSerializer


class GuideView(ViewSet):

    def list(self, request):
        '''list of all users'''
        guides = Guide.objects.all()
        serializer = GuideSerializer(guides, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            guide = Guide.objects.get(pk=pk)
            serializer = GuideSerializer(guide)
            return Response(serializer.data)
        except Guide.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
