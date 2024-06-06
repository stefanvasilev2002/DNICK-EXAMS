from django.db import models
from django.contrib.auth.models import User

class Balloon(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    passengers = models.IntegerField()


class Pilot(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    flight_hours = models.IntegerField()
    rank = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)
    year_created = models.IntegerField()
    flies_europe = models.BooleanField()


class Flight(models.Model):
    code = models.CharField(max_length=100)
    airport_takeoff = models.CharField(max_length=100)
    airport_landing = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='data/')
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class CompanyPilot(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)