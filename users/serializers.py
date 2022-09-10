from .models import *
from rest_framework import serializers
import uuid

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'displayName', 'profileImage']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorModel.id
    author_object = AuthorSerializer()
    class Meta:
        # TODO commentsSrc
        model = SessionListModel
        fields = ['object']
