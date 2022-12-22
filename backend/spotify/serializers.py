from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Album, Artist, Song, SongRating, AlbumRating

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
# class AllAlbumWithRatingSerializer(serializers.ModelSerializer):
#     rating = serializers.SerializerMethodField('get_rating')

#     class Meta:
#         model = Album
#         fields = ('id', 'rating')
    
#     def get_rating(self, value):
#         key = self.context.get('key')
#         if key is None:
#             return None
#         user = (Token.objects.get(key=key)).user
#         rating = AlbumRating.objects.filter(album=value, user=user).first()
#         if rating:
#             return rating.rating
#         return None

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField('get_rating')

    class Meta:
        model = Album
        fields = ('id', 'spotify_id', 'title', 'artist', 'release_date', 'cover', 'total_ratings', 'average_rating', 'rating')

    def get_rating(self, value):
        key = self.context.get('key')
        if key is None:
            return None
        user = (Token.objects.get(key=key)).user
        rating = AlbumRating.objects.filter(album=value, user=user).first()
        if rating:
            return rating.rating
        return None

class AlbumNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)
    
    def to_representation(self, value):
        return value.name

class AllSongWithRatingsSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField('get_rating')

    class Meta:
        model = Song
        fields = ('name', 'rating')

    def get_rating(self, value):
        key = self.context.get('key')
        if key is None:
            return None
        user = (Token.objects.get(key=key)).user
        rating = SongRating.objects.filter(user=user, song=value).first()
        if rating:
            return rating.liked
        return None


class AlbumDetailSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(read_only=True, many=True)
    songs = AllSongWithRatingsSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'spotify_id', 'title', 'artist', 'release_date', 'cover', 'total_ratings', 'average_rating', 'songs')
    