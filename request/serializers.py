from .models import *
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = "__all__"
        