from rest_framework import serializers
import uuid
from .models import *


class GroupSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSessionsModel
        fields = "__all__"
