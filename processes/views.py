from django.shortcuts import render
from rest_framework import viewsets
from .models import Process, AlgoUnit
from .serializers import AlgoUnitSerializer, ProcessSerializer
# Create your views here.
class ProcessView(viewsets.ModelViewSet):
    serializer_class = ProcessSerializer
    queryset = Process.objects.all()

class AlgoUnitView(viewsets.ModelViewSet):
    serializer_class = AlgoUnitSerializer
    queryset = AlgoUnit.objects.all()