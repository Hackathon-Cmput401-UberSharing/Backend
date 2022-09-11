from rest_framework import serializers
import uuid
from .models import *


class GroupSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSessionsModel
        fields = ['id', 'initiator', 'follower', 'location', 'time', 'success', 'ongoing']
