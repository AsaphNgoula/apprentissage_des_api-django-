from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_view(request,*args,**kwargs):
    #request => instance de HTTPrequest
    print(request.body) #byte string
    data = json.loads(request.body)
    data['headers']=dict(request.headers)
    data['params']=dict(request.GET)
    data['post-data']=dict(request.POST)
    print(request.headers)
    data['content_type']=request.content_type
    print(data)
    return JsonResponse(data)