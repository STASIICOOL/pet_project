from django.db import models
from city.models import City

# Create your models here.

class FoodPlace(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    item_type = models.CharField(max_length=150)
    working_hours = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    image = models.ImageField()
    food_place = models.ForeignKey(FoodPlace, on_delete=models.DO_NOTHING)
