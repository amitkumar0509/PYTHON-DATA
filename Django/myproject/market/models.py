from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)  # Links each album to a musician
    name = models.CharField(max_length=100)                         # Album name
    release_date = models.DateField()                               # Release date of the album
    num_stars = models.IntegerField()                               # Rating (e.g., out of 5)

# Create your models here.
