from django.db import models
from users.models import CustomUser
from statistics import mean
from django.db.models import Avg

'''
5CnpZV3q5BcESefcB3WJmz,0FgZKfoU2Br5sHOfvZKTI9,6pwuKxMUkNg673KETsXPUV,2Ek1q2haOnxVqhvVKqMvJe,7gsWAHLeT0w7es6FofOXk1,20r762YmB5HeofjMCiPMLv,7D2NdGvBHIavgLhmcwhluK,7mCeLbChyegbRwwKK5shJs,3WFTGIO6E3Xh4paEOBY9OU,4SZko61aMnmgvNhfhgTuD3,5ll74bqtkcXlKE7wwkMq4g,4Uv86qWpGTxf7fU7lG5X6F

The Beatles: 3WrFJ7ztbogyGnTHbHJFl2
'''

class Artist(models.Model):
  spotify_id = models.CharField(max_length=22, db_index=True, unique=True, default="aaaaaaaaaaaaaaaaaaaaa")
  name = models.CharField(max_length=140)
  rating = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)

  def _str_(self):
    return self.name

  def lookup_create(id, name):
    artist = Artist.objects.filter(spotify_id=id).first()
    if artist is None:
      artist = Artist.objects.create(spotify_id=id, name=name)
    return artist

class Album(models.Model):
  spotify_id = models.CharField(max_length=22, db_index=True, unique=True, default="aaaaaaaaaaaaaaaaaaaaa")
  title = models.CharField(max_length=140)
  artist = models.ManyToManyField(Artist)
  release_date = models.DateField()
  cover = models.URLField()
  user_ratings = models.ManyToManyField(CustomUser, through='AlbumRating', related_name='album_ratings')

  @property
  def total_ratings(self):
    return self.user_ratings.all().exclude(album_ratings=0).count()
  
  @property
  def average_rating(self):
    # return 5
    return AlbumRating.objects.filter(album=self).exclude(rating=0).aggregate(Avg('rating'))
    # all_ratings = AlbumRating.objects.filter(album=self).values_list('rating', flat=True)
    # return mean(list(all_ratings))


  
  def _str_(self):
    return self.title

class Song(models.Model):
  spotify_id = models.CharField(max_length=22, db_index=True, unique=True, default="aaaaaaaaaaaaaaaaaaaaa")
  name = models.CharField(max_length=140)
  track_number = models.PositiveIntegerField(default=0)
  album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
  artist = models.ManyToManyField(Artist)
  duration_ms = models.PositiveIntegerField(default=0)
  user_liked = models.ManyToManyField(CustomUser, through='SongRating', related_name='liked_songs')

  @property
  def likes(self):
    return SongRating.objects.filter(liked=True).count()

  @property
  def dislikes(self):
    return SongRating.objects.filter(liked=False).count()

  def _str_(self):
    return self.name
  
class AlbumRating(models.Model):
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField(blank=True, null=True, default=0)

class SongRating(models.Model):
  song = models.ForeignKey(Song, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  liked = models.BooleanField()
