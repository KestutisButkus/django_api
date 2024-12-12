from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AlbumReview(models.Model):
    SCORE_CHOICES = [
        ('1/10', '1/10'),
        ('2/10', '2/10'),
        ('3/10', '3/10'),
        ('4/10', '4/10'),
        ('5/10', '5/10'),
        ('6/10', '6/10'),
        ('7/10', '7/10'),
        ('8/10', '8/10'),
        ('9/10', '9/10'),
        ('10/10', '10/10'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.CharField(max_length=5, choices=SCORE_CHOICES)  # Tik pasirinktos reikšmės

    def __str__(self):
        return f'{self.album.name} - {self.user.username}'

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.album_review.album.name}'

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.username} on {self.album_review.album.name}'
