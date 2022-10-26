from django.db import models

# Create your models here.

'''
5CnpZV3q5BcESefcB3WJmz,0FgZKfoU2Br5sHOfvZKTI9,6pwuKxMUkNg673KETsXPUV,2Ek1q2haOnxVqhvVKqMvJe,7gsWAHLeT0w7es6FofOXk1,20r762YmB5HeofjMCiPMLv,7D2NdGvBHIavgLhmcwhluK,7mCeLbChyegbRwwKK5shJs,3WFTGIO6E3Xh4paEOBY9OU,4SZko61aMnmgvNhfhgTuD3,5ll74bqtkcXlKE7wwkMq4g,4Uv86qWpGTxf7fU7lG5X6F
'''
class Album(models.Model):
  title = models.CharField(max_length=140)
  artist = models.CharField(max_length=120)
  release_date = models.DateTimeField()
  cover = models.URLField()

  def _str_(self):
    return self.title
  