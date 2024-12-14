from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.exceptions import APIException
from django.contrib.auth.models import User
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer, AlbumSerializer, SongSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer

class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Priskiriamas prisijungęs vartotojas kuriant naują grupę
        serializer.save(user=self.request.user)

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Tik vartotojo grupės
        return Band.objects.filter(user=self.request.user)

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Priskiriamas prisijungęs vartotojas kuriant naują albumą
        serializer.save(user=self.request.user)

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Tik vartotojo albumai
        return Album.objects.filter(user=self.request.user)

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Priskiriamas prisijungęs vartotojas kuriant naują dainą
        serializer.save(user=self.request.user)

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Tik vartotojo dainos
        return Song.objects.filter(user=self.request.user)

class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return AlbumReview.objects.filter(pk=self.kwargs['pk'], user=self.request.user)

    def delete(self, request, *args, **kwargs):
        album_review = self.get_queryset()
        if album_review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            class CannotDeleteOtherUsersPosts(APIException):
                status_code = status.HTTP_403_FORBIDDEN
                default_detail = 'Negalima trinti svetimų įrašų!'
                default_code = 'forbidden'

            raise CannotDeleteOtherUsersPosts()

    def put(self, request, *args, **kwargs):
        album_review = self.get_queryset()
        if album_review.exists():
            return self.update(request, *args, **kwargs)
        else:
            class CannotEditOtherUsersPosts(APIException):
                status_code = status.HTTP_403_FORBIDDEN
                default_detail = 'Negalima koreguoti svetimų įrašų!'
                default_code = 'forbidden'

            raise CannotEditOtherUsersPosts()

class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_review_id = self.kwargs.get('album_review_pk')
        return AlbumReviewComment.objects.filter(album_review_id=album_review_id, user=self.request.user)

    def delete(self, request, *args, **kwargs):
        album_review_comment = self.get_queryset().filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            class CannotDeleteOtherUsersPosts(APIException):
                status_code = status.HTTP_403_FORBIDDEN
                default_detail = 'Negalima trinti svetimų įrašų!'
                default_code = 'forbidden'

            raise CannotDeleteOtherUsersPosts()

    def put(self, request, *args, **kwargs):
        album_review_comment = self.get_queryset().filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            class CannotEditOtherUsersPosts(APIException):
                status_code = status.HTTP_403_FORBIDDEN
                default_detail = 'Negalima koreguoti svetimų įrašų!'
                default_code = 'forbidden'

            raise CannotEditOtherUsersPosts()

class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlbumReviewLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_review_id = self.kwargs.get('album_review_pk')
        return AlbumReviewLike.objects.filter(album_review_id=album_review_id, user=self.request.user)

    def delete(self, request, *args, **kwargs):
        album_review_like = self.get_queryset().filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_like.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            class CannotDeleteOtherUsersPosts(APIException):
                status_code = status.HTTP_403_FORBIDDEN
                default_detail = 'Negalima trinti svetimų įrašų!'
                default_code = 'forbidden'

            raise CannotDeleteOtherUsersPosts()

    def put(self, request, *args, **kwargs):
        album_review_like = self.get_queryset().filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_like.exists():
            return self.update(request, *args, **kwargs)
        else:
            class CannotEditOtherUsersPosts(APIException):
                status_code = status.HTTP_403_FORBIDDEN
                default_detail = 'Negalima koreguoti svetimų įrašų!'
                default_code = 'forbidden'

            raise CannotEditOtherUsersPosts()

def home(request):
    return render(request, 'home.html')
