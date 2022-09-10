# Requirement
A user can start a session to a location (neighbourhood or an area)
other users within a certain distance will have the ability to see the sessions.
Other users can choose one to join.
Each session will expire based on a specific time chosen by whoever starting the group session.
Each session will have a maximum member count.


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profileImage = models.ImageField(verbose_name='profile_image',upload_to='',null=True)
    displayName = models.CharField(max_length=200)
    status = models.Boolean()
    

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
