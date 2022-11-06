from ctypes import alignment
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import AlbumSerializer
from .serializers import ArtistSerializer
from .models import Album, Artist

# Create your views here.

@api_view(['GET'])
def albums_list(request):
    if request.method == 'GET':
        data = Album.objects.all()
        serializer = AlbumSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def artists_list(request):
    if request.method == 'GET':
        data = Artist.objects.all()
        serializer = ArtistSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)