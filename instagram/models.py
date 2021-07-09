from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

Gender = (
  ('Male', 'Male'),
  ('Female', 'Female'),
)
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

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(username = instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()

  def __str__(self):
    return self.username.username

class Post(models.Model):
  picture = models.ImageField(upload_to='photos/')
  caption = models.CharField(max_length=3000)
  uploadedBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  posted = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.caption

  def save_picture(self, user):
    self.save()

  @classmethod
  def delete_picture(cls, id):
    cls.objects.filter(id=id).delete()
