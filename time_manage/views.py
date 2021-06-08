from django.shortcuts import render
from rest_framework import viewsets
from .models import TimeSession, DaySchedule
from .serializers import TimeSessionSerializer, DayScheduleSerializer
# Create your views here.

class TimeSessionView(viewsets.ModelViewSet):
    serializer_class = TimeSessionSerializer
    queryset = TimeSession.objects.all()

class DayScheduleView(viewsets.ModelViewSet):
    serializer_class = DayScheduleSerializer
    queryset = DaySchedule.objects.all()