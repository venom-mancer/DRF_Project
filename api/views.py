from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request):

    data = {}
    body = request.body
    try:
        data = json.load(body)
    except:
        pass
    
    data['headers'] = request.headers
    return JsonResponse(data)
