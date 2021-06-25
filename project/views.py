from django.shortcuts import render
from rest_framework import viewsets
from .models import Feature, Project, Tech, Task
from .serializers import FeatureSerializer, ProjectSerializer, TaskSerializer, TechSerializer
# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class FeatureView(viewsets.ModelViewSet):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()
    
class TechView(viewsets.ModelViewSet):
    serializer_class = TechSerializer
    queryset = Tech.objects.all()

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()