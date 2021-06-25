from analytics.models import Bot
from django.shortcuts import render
from .serializers import BotSerializer
from rest_framework import viewsets
from .models import Bot

# Create your views here.
class BotView(viewsets.ModelViewSet):
    serializer_class = BotSerializer
    queryset = Bot.objects.all()