from django.db import models



class Trip(models.Model):
    trip_number = models.CharField(max_length=100)
    bol_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)