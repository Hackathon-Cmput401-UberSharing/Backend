from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
import json
import uuid, random
from pathlib import Path
import os
import requests
import json

from users import views as user_views
#from sessions import session_views
#from messages import message_views

from rest_framework import status
from rest_framework.response import Response


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,uuid.UUID):
            return str(obj)
        return json.JSONEncoder.default(self,obj)

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        request.session['username'] = username
        request.session['password'] = password
        result = user_views.check_password(request)
        if (result.status_code != 200):
            print('error--------------', result.data)
            return render(request, "bad.html")
        else:
            # TODO success message
            print('Success')
            uid = request.session['id']
            print('[][][]' + str(uid))
            return redirect('http://127.0.0.1:8000/myProfile/?id={}'.format(uid))
