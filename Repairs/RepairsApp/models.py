from django.db import models
from django.contrib.auth.models import User


class Workshop(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    fixes_old_timers = models.BooleanField(default=False)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    country = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)


class Car(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField(default=50)
    color = models.CharField(max_length=100)


class WorkshopManufacturer(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Repair(models.Model):
    code = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Repairs')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
