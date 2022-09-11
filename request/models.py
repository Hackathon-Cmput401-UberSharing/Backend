import uuid
from django.db import models
from groupSessions.models import *
from users.models import *

# Create your models here.
class RequestModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sessionId = models.ForeignKey(GroupSessionsModel, related_name = ("session"), on_delete=models.CASCADE)
    status = models.BooleanField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    

