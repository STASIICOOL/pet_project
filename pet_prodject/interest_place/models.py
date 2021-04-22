from django.db import models
from city.models import City
# Create your models here.

class InterestingPlace(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)