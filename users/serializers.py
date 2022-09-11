from rest_framework import serializers
import uuid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user', 'id', 'profileImage', 'displayName', 'status']
