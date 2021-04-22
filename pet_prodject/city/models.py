from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=150)
    flag = models.ImageField(blank=True, null=True, upload_to="flags/")
    emblem = models.ImageField(blank=True, null=True, upload_to="emblems/")
    description = models.CharField(max_length=150)
    residents = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)
