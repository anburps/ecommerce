from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import productSerializer

# Create your views here.
@api_view()
def api_product(request):
    product=Product.objects.all()
    serializer =productSerializer(product,many=True)
    return Response(serializer.data)