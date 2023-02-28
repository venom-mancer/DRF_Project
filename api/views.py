from django.shortcuts import render
from django.http import JsonResponse
from api.models import TblProduct
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import json
from api.serializers import ProductSerializer





@api_view(['POST'])
def api_home(request):
    """
    DRF API VIEW
    """
    # if request.method != 'POST':
    #     return Response({"detail":"Get is not allowed"},status=405)

    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        data = product_serializer.data
        return Response(data)
