from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User
from users.models import *

# Create your models here.
class GroupSessionsModel(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    initiator = models.ForeignKey(UserModel, related_name=("initiator"), on_delete=models.CASCADE, null=True)
    follower = models.ManyToManyField(UserModel)
    '''
    follower = ArrayField(
        follower_object = models.ForeignKey(UserModel, related_name=("follower_obj"), on_delete=models.CASCADE, null=True),
        size=100,
    )
    '''
    location = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    success = models.DateTimeField()
    ongoing = models.BooleanField()
