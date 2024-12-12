from django.shortcuts import render
from rest_framework import viewsets
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer, AlbumSerializer, SongSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumReviewViewSet(viewsets.ModelViewSet):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer

class AlbumReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer

class AlbumReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
