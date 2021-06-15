from analytics.models import AutonomousAnalysis
from django.shortcuts import render
from .serializers import AutonomousAnalysisSerializer
from rest_framework import viewsets
from .models import AutonomousAnalysis

# Create your views here.
class AutonomousAnalysisView(viewsets.ModelViewSet):
    serializer_class = AutonomousAnalysisSerializer
    queryset = AutonomousAnalysis.objects.all()