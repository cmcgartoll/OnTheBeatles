from ctypes import alignment
from django.shortcuts import render
from rest_framework import generics
from .serializers import AlbumSerializer
from .serializers import ArtistSerializer
from .models import Album, Artist

# Create your views here.

class ArtistView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumView(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer