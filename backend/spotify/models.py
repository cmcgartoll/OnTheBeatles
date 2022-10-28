from enum import unique
from sre_constants import MAX_UNTIL
from django.db import models
import datetime

# Create your models here.

'''
5CnpZV3q5BcESefcB3WJmz,0FgZKfoU2Br5sHOfvZKTI9,6pwuKxMUkNg673KETsXPUV,2Ek1q2haOnxVqhvVKqMvJe,7gsWAHLeT0w7es6FofOXk1,20r762YmB5HeofjMCiPMLv,7D2NdGvBHIavgLhmcwhluK,7mCeLbChyegbRwwKK5shJs,3WFTGIO6E3Xh4paEOBY9OU,4SZko61aMnmgvNhfhgTuD3,5ll74bqtkcXlKE7wwkMq4g,4Uv86qWpGTxf7fU7lG5X6F

Kanye West: 5K4W6rqBFWDnAN6FQUkS6x
'''



class Artist(models.Model):
  spotify_id = models.CharField(max_length=22, db_index=True, unique=True, default="aaaaaaaaaaaaaaaaaaaaa")
  name = models.CharField(max_length=140)
  rating = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)

  def _str_(self):
    return self.name

class Album(models.Model):
  spotify_id = models.CharField(max_length=22, db_index=True, unique=True, default="aaaaaaaaaaaaaaaaaaaaa")
  title = models.CharField(max_length=140)
  artist = models.ManyToManyField(Artist)
  release_date = models.DateField()
  cover = models.URLField()
  likes = models.PositiveIntegerField(default=0)
  dislikes = models.PositiveIntegerField(default=0)
  

  def _str_(self):
    return self.title

# k = Artist(spotify_id="5K4W6rqBFWDnAN6FQUkS6x", name = "Kanye West")
# k.save()
# a = Album(spotify_id="4Uv86qWpGTxf7fU7lG5X6F", title="The College Dropout", artist=k, release_date=datetime.datetime(2004, 2, 10), cover="https://i.scdn.co/image/ab67616d0000b27325b055377757b3cdd6f26b78")
# a.save()
