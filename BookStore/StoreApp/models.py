from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = {
        ('bookUser', 'Book User'),
        ('author', 'Author'),
    }
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='bookUser')


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname


class BookUser(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name + " " + self.book.title
