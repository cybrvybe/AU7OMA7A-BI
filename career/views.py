from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CareerContactSerializer, CareerRoleSerializer, CompanySerializer
from .models import CareerContact, CareerRole, Company
# Create your views here.
class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class CareerContactView(viewsets.ModelViewSet):
    serializer_class = CareerContactSerializer
    queryset = CareerContact.objects.all()

class CareerRoleView(viewsets.ModelViewSet):
    serializer_class = CareerRoleSerializer
    queryset = CareerRole
