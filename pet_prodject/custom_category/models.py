from django.db import models
from city.models import City
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

class Post(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
