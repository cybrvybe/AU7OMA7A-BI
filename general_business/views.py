from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrganizationSerializer, RoleSerializer, VentureSerializer
from .models import Organization, Venture, Role

# Create your views here.
class OrganizationView(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

class VentureView(viewsets.ModelViewSet):
    serializer_class = VentureSerializer
    queryset = Venture.objects.all()

class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()