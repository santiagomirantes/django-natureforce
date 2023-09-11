from django.db import models
from django.conf import settings
import os

# Create your models here.

class Photo(models.Model) :
    name = models.CharField(max_length = 100)
    year = models.IntegerField()
    file = models.FileField()
    artist = models.CharField(max_length = 100)
    description = models.TextField(default="A short description of the picture.")

    def __str__(self):
        return f"{self.name} - {self.artist}"

class Artist(models.Model) :
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.email}"