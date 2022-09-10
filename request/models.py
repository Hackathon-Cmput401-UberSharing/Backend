import uuid
from django.db import models


# Create your models here.
class RequestModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sessionId = models.ForeignKey(SessionModel, related_name = ("session"), on_delete=models.CASCADE)
    status = models.BooleanField()
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    currentLocation = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)    
    expirationDate = models.DateField()
    maxUser = models.IntegerField()
    lastModifiedDate = models.DateField()

    

