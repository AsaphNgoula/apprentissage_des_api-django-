from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_view(request,*args, **kwargs):
    data={
        'name':'Asaph',
        'language':'python',
    }
    return JsonResponse(data)