from django.urls import path
from .views import ArtistView, AlbumView

urlpatterns = [
    path('artist/', ArtistView.as_view()),
    path('album/', AlbumView.as_view()),
]
