from django.shortcuts import render
from rest_framework import viewsets
from .models import Feature, Project
from .serializers import FeatureSerializer, ProjectSerializer
# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class FeatureView(viewsets.ModelViewSet):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()
    