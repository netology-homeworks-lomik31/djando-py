from django.db import models
from django.utils.timezone import now

class Sensor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=False)
    value = models.IntegerField(blank=False)
    date = models.DateTimeField(default=now, blank=False)
