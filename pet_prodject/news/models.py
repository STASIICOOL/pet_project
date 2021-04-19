from django.db import models
from city.models import City
# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField()
    image = models.ImageField()
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)
