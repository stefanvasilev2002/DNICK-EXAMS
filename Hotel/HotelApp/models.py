from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    POSITIONS = [
        ('C', 'cleaner'),
        ('M', 'manager'),
        ('R', 'receptionist')
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job_description = models.TextField()
    year_employed = models.IntegerField()
    type_of_employee = models.CharField(max_length=3, choices=POSITIONS)


class Room(models.Model):
    number = models.IntegerField()
    beds = models.IntegerField()
    has_terrace = models.BooleanField()
    is_cleaned = models.BooleanField()


class RoomCleaner(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    cleaner = models.ForeignKey(Employee, on_delete=models.CASCADE)


class HotelReservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='data/')
    is_confirmed = models.BooleanField(default=False)
    employee_confirmed = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

