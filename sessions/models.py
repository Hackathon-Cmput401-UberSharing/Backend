from django.db import models

# Create your models here.
class SessionModel(models.Model):
    id = models.CharField(max_length=200)
    initiator = models.ForeignKey(UserModel, related_name=("initiator"), on_delete=models.CASCADE, null=True)
    follower = ArrayField(
        follower_object = models.ForeignKey(UserModel, related_name=("follower_obj"), on_delete=models.CASCADE, null=True),
        size=100,
    )
    location = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    success = models.DateTimeField()
    ongoing = models.BooleanField()
