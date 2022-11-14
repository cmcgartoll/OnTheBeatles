from django.contrib import admin
from django.urls import path
from .views import albums_list, artists_list, album_detail

urlpatterns = [
    path('artists/', artists_list ),
    path('albums/', albums_list),
    path('album/<int:id>/', album_detail),
]
