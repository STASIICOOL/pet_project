from django.db import models
from city.models import City
# Create your models here.

class Housing(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    checkin_time = models.CharField(max_length=150)
    checkout_time = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

class Number_housing(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.CharField()
    city = models.ForeignKey(Housing, on_delete=models.DO_NOTHING)