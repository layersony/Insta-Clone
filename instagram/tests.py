from django.test import TestCase
from .models import Location, Profile, Post


class TestLocation(TestCase):
  def setUp(self):
    self.location = Location(location='Machakos')

  def TearDown(self):
    Location.objects.all().delete()

# Create your tests here.
