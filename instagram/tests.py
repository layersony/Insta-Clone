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

  def test_deleteLocation(self):
    self.location.saveLocation()
    self.location2 = Location.objects.create(location='Mombasa')
    Location.deleteLocation(self.location2.id)
    self.assertTrue(len(Location.objects.all())==1)

  def test_updateLocation(self):
    update_term = 'Mombasa'
    self.location.saveLocation()
    Location.updateLocation(self.location.id, update_term)  
    updated_one = Location.objects.get(id=self.location.id)
    self.assertEqual(updated_one.location, 'Mombasa')

class TestProfile(TestCase):
  def setUp(self):
    self.new_user = User(username = "layersony", email = "layersony@gmail.com",password = "layersony1234")
    self.new_user.save()

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()

