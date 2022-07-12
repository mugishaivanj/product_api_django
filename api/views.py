from itertools import product
from math import prod
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
"""@api_view(['GET'])
def apiOverview(request):
    api_urls={

    'List':'/product-list',
    'Detail-View':'/product-detail<int:id>/',
    'Create':'/product-create/',
    'Update':'/product-update/<int:id>',
    'Delete':'/product-delete/<int:id>',
    }

    return Response (api_urls);
"""
@api_view(['GET'])
def ShowAll(request):
    product=Product.objects.all()
    serializer=ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    product=Product.objects.get(id=pk)
    serializer=ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def CreateProduct(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def UpdateProduct(request):
    product=Product.objects.all()
    serializer=ProductSerializer(instance=product, request=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def DeleteProduct(request, pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response('item deleted succesfully')