from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from groupSessions.serializers import *

# Create your views here.

@api_view(['GET'])
def getRequests(request):
    if request.method == 'GET':
        requests = RequestModel.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data, status=200)

@api_view(['POST'])
def createRequest(request):
    if request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Request created!:", status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(['POST'])
def acceptRequest(request,userId,sessionId):
    if request.method == 'POST':
        user = UserModel.objects.get(pk=userId)
        session = GroupSessionsModel.obejcts.get(pk=sessionId)
        if user and session:
            # fields = ['id', 'initiator', 'follower', 'location', 'time', 'success', 'ongoing']
            newFollower = session.follower.append(user)
            serializer = GroupSessionsSerializer(session.id, session.initiator, newFollower, session.location, session.time, session.sucess, session.ongoing)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response({"message":"Failed to accept request!","data":serializer.data}, status=400)
        

@api_view(['POST'])
def rejectRequest(request,requestId):
    if request.method == 'POST':
        currentRequest = RequestModel.object.get(pk=requestId)
        if currentRequest: 
            serializer = RequestSerializer(currentRequest.id, currentRequest.sessionId, False, currentRequest.user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            else:
                return Response({"message": "Failed to reject request!", "data": serializer.data}, status=400)



