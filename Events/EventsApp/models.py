from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    events_count = models.IntegerField()


class Event(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    image = models.ImageField(upload_to='data/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)
    bands = models.CharField(max_length=200, default='')
    num_participants = models.IntegerField(default=0)


class EventBand(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
