from django.shortcuts import render
from rest_framework import viewsets
from .models import Process
from .serializers import ProcessSerializer
# Create your views here.
class ProcessView(viewsets.ModelViewSet):
    serializer_class = ProcessSerializer
    queryset = Process.objects.all()
