from rest_framework import serializers
from .models import Album, Artist, Song

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

class SongDetailSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(read_only=True, many=True)
    class Meta:
        model = Song
        fields = ('id', 'spotify_id', 'name', 'track_number', 'album', 'artist', 'duration_ms', 'likes', 'dislikes')

class SongNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('name',)
    
    def to_representation(self, value):
        return value.name

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(read_only=True, many=True)
    class Meta:
        model = Album
        fields = ('id', 'spotify_id', 'title', 'artist', 'release_date', 'cover', 'total_ratings', 'average_rating')

class AlbumNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)
    
    def to_representation(self, value):
        return value.name

class AlbumDetailSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(read_only=True, many=True)
    songs = SongNameSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'spotify_id', 'title', 'artist', 'release_date', 'cover', 'total_ratings', 'average_rating', 'songs')
        