from django.db import models

# Create your models here.

class FoodPlace(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField()
    longitude =
    latitude =