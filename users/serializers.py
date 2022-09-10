from rest_framework import serializers
import uuid

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionModel
        fields = ['user', 'id', 'profileImage', 'displayName']
