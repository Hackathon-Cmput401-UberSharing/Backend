from itertools import chain
from logging import exception
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import uuid, random
from datetime import datetime
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
@api_view(['GET', 'POST'])
def check_password(request):
    if request.method == 'GET':
        message = {'message:', '200'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        username = request.session['username']
        password = request.session['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            message = {'message:', '200'}
            request.session['id'] = user.id
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'message:', '400'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

def myProfile(request):
    return Response(message, status=status.HTTP_200_OK)
