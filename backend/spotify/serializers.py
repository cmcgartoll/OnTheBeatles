from rest_framework import serializers
from .models import Album, Artist

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'spotify_id', 'title', 'artist', 'release_date', 'cover', 'likes', 'dislikes')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'spotify_id', 'name', 'rating')
        