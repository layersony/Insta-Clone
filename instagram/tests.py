from django.test import TestCase
from .models import Location, Profile, Post


class TestLocation(TestCase):
  def setUp(self):
    self.location = Location(location='Machakos')

  def TearDown(self):
    Location.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.location, Location))

  def test_saveLocation(self):
    self.location.save()
    location = Location.objects.all()
    self.assertTrue(len(location)>0)
