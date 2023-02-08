from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_lenght=100)
    roll_number = models.CharField(max_lenght=100)
