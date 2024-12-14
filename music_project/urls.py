from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import admin
from .views import BandList, BandDetail, AlbumList, AlbumDetail, SongList, SongDetail, AlbumReviewList, \
    AlbumReviewDetail, AlbumReviewCommentList, AlbumReviewCommentDetail, AlbumReviewLikeList, AlbumReviewLikeDetail


urlpatterns = [
    path('bands/', BandList.as_view(), name='band-list'),
    path('bands/<int:pk>/', BandDetail.as_view(), name='band-detail'),
    path('albums/', AlbumList.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
    path('songs/', SongList.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongDetail.as_view(), name='song-detail'),
    path('albumreviews/', AlbumReviewList.as_view(), name='albumreview-list'),
    path('albumreviews/<int:pk>/', AlbumReviewDetail.as_view(), name='albumreview-detail'),
    path('albumreviewcomments/', AlbumReviewCommentList.as_view(), name='albumreviewcomment-list'),
    path('albumreviewcomments/<int:pk>/', AlbumReviewCommentDetail.as_view(), name='albumreviewcomment-detail'),
    path('albumreviewlikes/', AlbumReviewLikeList.as_view(), name='albumreviewlike-list'),
    path('albumreviewlikes/<int:pk>/', AlbumReviewLikeDetail.as_view(), name='albumreviewlike-detail'),
]
