from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike

class BandSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Tik vartotojo vardas

    class Meta:
        model = Band
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source='band.name')  # Grupės pavadinimas
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source='album.name')  # Albumo pavadinimas
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Song
        fields = '__all__'


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReview
        fields = '__all__'

class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewComment
        fields = '__all__'

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewLike
        fields = '__all__'
