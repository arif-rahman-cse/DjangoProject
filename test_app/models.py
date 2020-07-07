from django.db import models

# Create your models here.
#This is simple destination class 
"""
class Destination:
    id : int
    name : str
    img : str
    desc : str
    price : int
    offer : bool
"""
#Convert a class in a Model
class Destination(models.Model):
    # Here we need to equal sign because we are assigning a value 
    name = models.CharField(max_length=100) # Database filed length
    img = models.ImageField(upload_to='pics') # Image Upload location
    desc = models.TextField() 
    price = models.IntegerField()
    offer = models.BooleanField(default=False) # Deafult value is false