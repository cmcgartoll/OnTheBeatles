from django.contrib import admin
from django.urls import path
from .views import albums_list, artists_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', artists_list ),
    path('albums/', albums_list),
]
