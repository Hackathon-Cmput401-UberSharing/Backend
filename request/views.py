from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    