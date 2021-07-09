from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

Gender = (
  ('Male', 'Male'),
  ('Female', 'Female'),
)
class Location(models.Model):
  location = models.CharField(max_length=100)

  def saveLocation(self):
    self.save()

  @classmethod
  def deleteLocation(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def updateLocation(cls, id, locaUpdate):
    cls.objects.filter(id=id).update(location=locaUpdate)

  def __str__(self):
    return self.location

class Profile(models.Model):
  profilePic = models.ImageField(upload_to='photos/', null=True)
  fullName= models.CharField(max_length=255, null=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = HTMLField(null=True)
  phoneNumber = models.IntegerField(null=True)
  gender = models.CharField(choices=Gender, default='Male', null=True, max_length=50)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(username=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

  def __str__(self):
    return self.username.username

  @classmethod
  def searchProfile(cls, searchTerm):
    profiles = User.objects.filter(username__icontains=searchTerm)
    return profiles

class Post(models.Model):
  picture = models.ImageField(upload_to='photos/')
  caption = models.CharField(max_length=3000)
  uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  posted = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.caption

  def save_picture(self):
    self.save()

  @classmethod
  def delete_picture(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def update_caption(cls, id, caption):
    cls.objects.filter(id=id).update(caption = caption)

  @classmethod
  def user_pictures(cls, username):
    pics = cls.objects.filter(uploadedBy__username = username)
    return pics

  @classmethod
  def all_pictures(cls):
    all_pics = cls.objects.all()
    return all_pics

class Comments(models.Model):
  comment = models.CharField(max_length=200, null=True, blank=True)
  pic = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  