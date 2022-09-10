from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET', 'POST'])
def getRequests(request):
    if request.method = 'GET':
        requests = Request.objects.all()
        serializer = ItemSerializer(requests, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def acceptRequest(request):
    if request.method = 'POST':
        result = views.acceptRequest(request)

def rejectRequest(request):
    if request.method = 'POST':
        result = views.rejectRequest(request)


    