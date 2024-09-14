from django.db import models
from django.contrib.auth.models import User


class Painter(models.Model):
    STYLES = {
        "IMP": "Impressionism",
        "POP": "Pop Art",
        "GRA": "Graffiti"
    }
    name_and_surname = models.CharField(max_length=100)
    style = models.CharField(max_length=10, choices=STYLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=100)


class Painting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
