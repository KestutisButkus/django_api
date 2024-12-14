from django.db import models
from django.contrib.auth.models import User

# Represents a musical band / Muzikinė grupė
class Band(models.Model):
    name = models.CharField(max_length=100)  # Name of the band / Grupės pavadinimas
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User associated with the band / Naudotojas, susijęs su grupe

    def __str__(self):
        return self.name  # String representation of the band / Grupės teksto atvaizdavimas

# Represents an album belonging to a band / Albumas, priklausantis grupei
class Album(models.Model):
    name = models.CharField(max_length=100)  # Name of the album / Albumo pavadinimas
    band = models.ForeignKey(Band, on_delete=models.CASCADE)  # Band associated with the album / Grupė, susijusi su albumu
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the album / Naudotojas, sukūręs albumą

    def __str__(self):
        return self.name  # String representation of the album / Albumo teksto atvaizdavimas

# Represents a song in an album / Daina, esanti albume
class Song(models.Model):
    name = models.CharField(max_length=100)  # Name of the song / Dainos pavadinimas
    duration = models.DurationField()  # Duration of the song / Dainos trukmė
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Album the song belongs to / Albumas, kuriam priklauso daina
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who added the song / Naudotojas, pridėjęs dainą

    def __str__(self):
        return self.name  # String representation of the song / Dainos teksto atvaizdavimas

# Represents a review for an album / Albumo apžvalga
class AlbumReview(models.Model):
    SCORE_CHOICES = [
        (1, '1 out of 10'),
        (2, '2 out of 10'),
        (3, '3 out of 10'),
        (4, '4 out of 10'),
        (5, '5 out of 10'),
        (6, '6 out of 10'),
        (7, '7 out of 10'),
        (8, '8 out of 10'),
        (9, '9 out of 10'),
        (10, '10 out of 10'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the review / Naudotojas, parašęs apžvalgą
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Album being reviewed / Albumas, kuriam parašyta apžvalga
    content = models.TextField()  # Review content / Apžvalgos turinys
    score = models.IntegerField(choices=SCORE_CHOICES)  # Score given to the album / Albumui suteiktas įvertinimas

    def __str__(self):
        return f'{self.album.name} - {self.user.username}'  # String representation of the review / Apžvalgos teksto atvaizdavimas

# Represents a comment on an album review / Komentaras prie albumo apžvalgos
class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the comment / Naudotojas, parašęs komentarą
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)  # Review being commented on / Apžvalga, kuriai parašytas komentaras
    content = models.TextField()  # Comment content / Komentaro turinys

    def __str__(self):
        return f'Comment by {self.user.username} on {self.album_review.album.name}'  # String representation of the comment / Komentaro teksto atvaizdavimas

# Represents a like on an album review / Patiktukas prie albumo apžvalgos
class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who liked the review / Naudotojas, paspaudęs patiktuką
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)  # Review being liked / Apžvalga, kuriai skirtas patiktukas

    def __str__(self):
        return f'Like by {self.user.username} on {self.album_review.album.name}'  # String representation of the like / Patiktuko teksto atvaizdavimas
