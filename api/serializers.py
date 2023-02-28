
from .models import TblProduct
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = TblProduct
        fields = ['title','content','price','sell_price','get_discount']
