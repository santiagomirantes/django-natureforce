from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="uploadedImages", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.image}"
    
class Message(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length=1000)
    transmitter = models.CharField(max_length = 250)
    receiver = models.CharField(max_length = 250)

    def __str__(self):
      return f"{self.transmitter} to {self.receiver}"
