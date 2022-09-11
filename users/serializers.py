from rest_framework import serializers
import uuid
from users.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user', 'id', 'profileImage', 'displayName', 'status']

'''
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginInformationModel
        fields = ['id', 'username', 'password']
        '''
