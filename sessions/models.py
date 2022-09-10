from django.db import models

# Create your models here.
class SessionModel(models.Model):
    uid1 = models.CharField(max_length=200)
    uid2 = models.CharField(max_length=200)
    location1 = models.CharField(max_length=200)
    location2 = models.CharField(max_length=200)
    dest1 = models.CharField(max_length=200)
    dest2 = models.CharField(max_length=200)
    time1 = models.DateTimeField(auto_now=True)
    time2 = models.DateTimeField(auto_now=True)
    ongoing = models.BooleanField()
