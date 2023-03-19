from django.shortcuts import render
from django.http import JsonResponse
from api.models import TblProduct
from rest_framework import generics , mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import json
from django.http import Http404 
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer


class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView):

    queryset = TblProduct.objects.all()
    serializer = ProductSerializer
    def get(self , request):
        return self.list(request)
     
    # def post()

@api_view(['POST'])
def api_home(request):
    """
    DRF API VIEW
    """
    # if request.method != 'POST':
    #     return Response({"detail":"Get is not allowed"},status=405)

    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid(raise_exception=True):
        data = product_serializer.data
        return Response(data)
    return Response({"invalid" :"invalid data"})


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = TblProduct.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):

    queryset = TblProduct.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    
    queryset = TblProduct.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST','GET'])
def get_alt_view(request,pk=None):

    if request.method == "GET":
        if pk is not None:

            obj = get_object_or_404(TblProduct,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response()

        queryset = TblProduct.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)

    if request.method == "POST":

        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid(raise_exception=True):
            title = product_serializer.validated_data.get('title')
            content = product_serializer.validated_data.get('content')
            if content is None:
                content = title
            product_serializer.save(content=content)
            return Response(product_serializer.data)
        return Response({"invalid" :"invalid data"},status=400)


class ProductUpdateAPIView(generics.UpdateAPIView):
    
    queryset = TblProduct.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = 'pk'

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    
    queryset = TblProduct.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self,instance):
        super().perform_destroy(instance)