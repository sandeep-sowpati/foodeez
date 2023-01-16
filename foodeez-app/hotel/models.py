"""
Model for Hotels
"""

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from PIL import Image


class RestaurantLog(models.Model):
    """Model for Restaurant."""
    manager=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    street=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    pincode=models.CharField(max_length=6)
    restimage = models.ImageField(upload_to='restaurant/rest', blank=True)

    def __str__(self):
        return self.name + " at " + self.city

class RestaurantItems(models.Model):
    """Model for Food Items."""
    restaurantid=models.ForeignKey(RestaurantLog,on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    category=models.CharField(max_length=150)
    price=models.CharField(max_length=6)
    availability=models.CharField(max_length=6)
    foodimage=models.ImageField(upload_to='restaurant/food',blank=True)

    def __str__(self):
        return self.foodname