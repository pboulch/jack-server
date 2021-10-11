from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class UserRoom(User):
    friendly_name = models.CharField(max_length=50)

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    access_code = models.CharField(max_length=200, unique=True)
    spotify_token = models.CharField(max_length=200, unique=True)
    user = models.OneToOneField(UserRoom, on_delete=CASCADE)


