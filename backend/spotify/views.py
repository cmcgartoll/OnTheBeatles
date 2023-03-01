from ctypes import alignment
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AlbumDetailSerializer, AlbumSerializer, ArtistSerializer
from .models import Album, Artist, SongRating, Song, AlbumRating
from users.models import CustomUser

# Create your views here.

class AlbumsListView(APIView):
    def get(self, request):
        data = Album.objects.all()
        key = request.headers.get('Authorization') 
        serializer = AlbumSerializer(data, context={'request': request, 'key': key}, many=True)
        return Response(serializer.data)

class AlbumDetailView(APIView):
    def get(self, request, id):
        try:
            album = Album.objects.get(id=id)
            key = request.headers.get('Authorization')
            serializer = AlbumDetailSerializer(album, context={'request': request, 'key': key})
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ArtistListView(APIView):
    def get(self, request):
        data = Artist.objects.all()
        serializer = ArtistSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

class AlbumLikesView(APIView):
    # def get(self, request, id):
    #     try:
    #         album = Album.objects.get(id=id)
    #         key = request.headers.get('Authorization')
    #         print(key)
    #         if key is None:
    #             return Response({'error': 'Authentication is null'}, status=status.HTTP_400_BAD_REQUEST)
    #         user = CustomUser.objects.get_user_from_token(key=key)
    #         songs = SongRating.objects.filter(user=user, song__album=album)
    #         print(songs)
    #         serializer = SongRatingSerializer(songs, many=True)
    #         print(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request, id):
        album = Album.objects.get(id=id)
        key = request.headers.get('Authorization')
        liked = request.data.get('liked')
        disliked = request.data.get('disliked')
        print(liked)
        print(disliked)
        if key is None:
            return Response({'error': 'Authentication is null'}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.get_user_from_token(key=key)
        song_name = request.data.get("song_name")
        song = Song.objects.filter(album=album, name=song_name).first()
        song_rating = SongRating.objects.filter(user=user, song=song).first()
        print(song_rating)
        if not song_rating:
            SongRating.objects.create(song=song, user=user, liked=liked)
            return Response(status=status.HTTP_201_CREATED)
        liked_val = song_rating.liked
        print(liked_val)
        if (liked_val and liked) or (not liked_val and disliked):
            song_rating.delete()
            return Response(status=status.HTTP_200_OK)
        try:
            song_rating.update(liked=(not liked_val))
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AlbumRatingView(APIView):
    def post(self, request, id):
        album = Album.objects.get(id=id)
        key = request.headers.get('Authorization')
        rating = request.data.get('rating')
        print(rating)
        if key is None:
            return Response({'error': 'Authentication is null'}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.get_user_from_token(key=key)
        album_rating = AlbumRating.objects.filter(album=album, user=user)
        if not album_rating:
            AlbumRating.objects.create(album=album, user=user, rating=rating)
            return Response(status=status.HTTP_201_CREATED)
        try:
            if rating != 0:
                album_rating.update(rating=rating)
                return Response(status=status.HTTP_200_OK)
            else:
                album_rating.update(rating=None)
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)