from django.db import models
from django.conf import settings
import os

# Create your models here.

class Photo(models.Model) :
    name = models.CharField(max_length = 100)
    year = models.IntegerField()
    file = models.FileField()
    artist = models.CharField(max_length = 100)

class Artist(models.Model) :
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()

class User(models.Model) :
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    profilePicture = models.FileField(
        upload_to='uploadedImages/',
        default=os.path.join(settings.MEDIA_ROOT, 'default_files', 'default_profile.png')
    )