from rest_framework import serializers
from .models import Album, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'spotify_id', 'name', 'rating')

class ArtistNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)
    
    def to_representation(self, value):
        return value.name

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(read_only=True, many=True)
    class Meta:
        model = Album
        fields = ('id', 'spotify_id', 'title', 'artist', 'release_date', 'cover', 'likes', 'dislikes')
        