from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import admin
from .views import BandViewSet, AlbumReviewViewSet, AlbumReviewCommentViewSet, AlbumViewSet, SongViewSet, AlbumReviewLikeViewSet

# urlpatterns = [
#     path('', BandViewSet.as_view()),
#     path('', AlbumViewSet.as_view()),
#     path('', SongViewSet.as_view()),
#     path('', AlbumReviewViewSet.as_view()),
#     path('', AlbumReviewCommentViewSet.as_view()),
#     path('', AlbumReviewLikeViewSet.as_view()),
# ]

# router = DefaultRouter()
# router.register(r'bands', BandViewSet, basename='band')
# router.register(r'albums', AlbumViewSet, basename='album')
# router.register(r'songs', SongViewSet, basename='song')
# router.register(r'albumreviews', AlbumReviewViewSet, basename='albumreview')
# router.register(r'albumreviewcomments', AlbumReviewCommentViewSet, basename='albumreviewcomment')
# router.register(r'albumreviewlikes', AlbumReviewLikeViewSet, basename='albumreviewlike')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('bands/', BandViewSet.as_view(), name='band-list'),
    path('albums/', AlbumViewSet.as_view(), name='album-list'),
    path('songs/', SongViewSet.as_view(), name='song-list'),
    path('albumreviews/', AlbumReviewViewSet.as_view(), name='albumreview-list'),
    path('albumreviewcomments/', AlbumReviewCommentViewSet.as_view(), name='albumreviewcomment-list'),
    path('albumreviewlikes/', AlbumReviewLikeViewSet.as_view(), name='albumreviewlike-list'),
]
