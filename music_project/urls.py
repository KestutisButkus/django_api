from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BandViewSet, AlbumViewSet, SongViewSet, AlbumReviewViewSet, AlbumReviewCommentViewSet, AlbumReviewLikeViewSet

router = DefaultRouter()
router.register(r'bands', BandViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'album-reviews', AlbumReviewViewSet)
router.register(r'album-review-comments', AlbumReviewCommentViewSet)
router.register(r'album-review-likes', AlbumReviewLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
