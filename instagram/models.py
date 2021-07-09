from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

Gender = ()
class Location(models.Model):
  location = models.CharField(max_length=100)

  def __str__(self):
    return self.location

class Profile(models.Model):
  pass

class Post(models.Model):
  pass
