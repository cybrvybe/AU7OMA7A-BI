from metrics.serializers import MetricSerializer
from django.shortcuts import render
from rest_framework import viewsets, views
from .models import Metric
# Create your views here.
class MetricView(viewsets.ModelViewSet):
    serializer_class = MetricSerializer
    queryset = Metric.objects.all()