from rest_framework import serializers
import uuid

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionModel
        fields = ['id', 'initiator', 'follower', 'location', 'time', 'success', 'ongoing']
