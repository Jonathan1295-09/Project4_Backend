from django.db import models

# Create your models here.

class personalBest(models.Model):
    Cardio = models.CharField(max_length=200)
    Benchpress = models.CharField(max_length=200)
    Deadlift = models.CharField(max_length=200)
    Squat = models.CharField(max_length=200)
    Shoulderpress = models.CharField(max_length=200)