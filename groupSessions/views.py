from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from groupSessions.serializers import *
from users.serializers import *

# Create your views here.

@api_view(['GET'])
def getSessions(request):
    if request.method == 'GET':
        groupSessions = GroupSessionsModel.objects.all()
        serializer = GroupSessionsSerializer(groupSessions, many=True)
        return Response(serializer.data, status=200)

@api_view(['POST'])
def startSession(request):
    if request.method == 'POST':
        serializer = GroupSessionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Session created!:", status=201)
        else:

            return Response(serializer.errors, status=400)


