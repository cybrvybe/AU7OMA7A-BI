from django.shortcuts import render
from .serializers import ModuleSerializer
from rest_framework import viewsets
from .models import Module
# Create your views here.
class ModuleView(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
