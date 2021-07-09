from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

Gender = ()
class Location(models.Model):
  location = models.CharField(max_length=100)

  def __str__(self):
    return self.location

class Profile(models.Model):
  profilePic = models.ImageField(upload_to='photos/', null=True)
  fullName= models.CharField(max_length=255, null=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='username')
  bio = HTMLField(null=True)
  phoneNumber = models.IntegerField(null=True)
  gender = models.CharField(choices=Gender, default='Male', null=True)

class Post(models.Model):
  pass
