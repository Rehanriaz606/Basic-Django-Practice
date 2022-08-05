from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
from tkinter import CASCADE
from django.db import models
from matplotlib.pyplot import title
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=400)

    def __str__(self):
        return self.name
    

class movies(models.Model):
    title=models.CharField(max_length=200)
    release_year=models.IntegerField()
    daily_rate=models.FloatField()
    Genre= models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created= models.DateTimeField(default=timezone.now)


