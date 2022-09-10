from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class AuthorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profileImage = models.ImageField(verbose_name='profile_image',upload_to='',null=True)
    displayName = models.CharField(max_length=200)

class SessionListModel(models.Model):
    object = models.ForeignKey(AuthorModel, related_name=("session_list"), on_delete=models.CASCADE)




