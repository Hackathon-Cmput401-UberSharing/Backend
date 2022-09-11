from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

@api_view(['GET'])
def getRequests(request):
    if request.method = 'GET':
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        serializer.save()
        return Response(serializer.data)



@api_view(['POST'])
def acceptRequest(request,userId,sessionId):
    if request.method = 'POST':
        user = Usermodel.objects.get(pk=userId)
        session = SessionModel.obejcts.get(pk=sessionId)
        if user and session:
            # fields = ['id', 'initiator', 'follower', 'location', 'time', 'success', 'ongoing']
            newFollower = session.follower.append(user)
            serializer = SessionSerializer(session.id, session.initiator, newFollower, session.location, session.time, session.sucess, session.ongoing)
            serializer.save()
            return Response(serializer.data)
        

@api_view(['POST'])
def rejectRequest(request,requestId):
    if request.method = 'POST':
        currentRequest = Request.object.get(pk=requestId)
        if currentRequest: 
            serializer = RequestSerializer(currentRequest.id, currentRequest.sessionId, False, currentRequest.user)
            serializer.save()
            return Response(serializer.data)



