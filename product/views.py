from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Service
from .serializers import ProductSerializer, ServiceSerializer
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

