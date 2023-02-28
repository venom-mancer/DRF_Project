from django.shortcuts import render
from django.http import JsonResponse
from api.models import TblProduct
from django.forms.models import model_to_dict
import json


def api_home(request):

    data = {}
    model_data = TblProduct.objects.order_by("?").first()
    if model_data:
        data = model_to_dict(model_data, fields=['id' , 'price'])

    return JsonResponse(data , headers = {"content_type" : "application/json"})
