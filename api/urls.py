"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music_project.views import home
urlpatterns = [
    # path('admin/', admin.site.urls),  # Administratoriaus puslapis
    # path('', home, name='home'),  # Pagrindinis puslapis
    # path('bands/', BandViewSet.as_view(), name='band-list'),
    # path('albums/', AlbumViewSet.as_view(), name='album-list'),
    # path('songs/', SongViewSet.as_view(), name='song-list'),
    # path('albumreviews/', AlbumReviewViewSet.as_view(), name='albumreview-list'),
    # path('albumreviewcomments/', AlbumReviewCommentViewSet.as_view(), name='albumreviewcomment-list'),
    # path('albumreviewlikes/', AlbumReviewLikeViewSet.as_view(), name='albumreviewlike-list'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),  # Pagrindinis maršrutas nukreipia į home vaizdą
    path('admin/', admin.site.urls),
    path('api/', include('music_project.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # REST framework autentifikacija
]
