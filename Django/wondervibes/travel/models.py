from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class TravelPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    activities = models.TextField()  # Comma-separated activities

    def __str__(self):
        return self.title
# Create your models here.
