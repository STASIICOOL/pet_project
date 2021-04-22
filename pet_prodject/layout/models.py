from django.db import models

# Create your models here.

class Layout(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    directory_layout = models.CharField(max_length=500)
    price = models.CharField(max_length=100)