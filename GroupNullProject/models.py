from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=80)
    numCredits = models.IntegerFiel()

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name