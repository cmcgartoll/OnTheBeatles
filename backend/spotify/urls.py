from django.urls import path
from .views import ArtistListView, AlbumDetailView, AlbumsListView, AlbumLikesView, AlbumRatingView

urlpatterns = [
    path('artists/', ArtistListView.as_view()),
    path('albums/', AlbumsListView.as_view()),
    path('album/<int:id>/', AlbumDetailView.as_view()),
    path('album-likes/<int:id>/', AlbumLikesView.as_view()),
    path('album-rating/<int:id>/', AlbumRatingView.as_view())
]
