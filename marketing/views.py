from django.shortcuts import render
from rest_framework import viewsets
from .models import Campaign, Brand, SocialMediaAccount
from .serializers import BrandSerializer, CampaignSerializer, SocialMediaAccountSerializer
# Create your views here.

class CampaignView(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

class BrandView(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class SocialMediaAccountView(viewsets.ModelViewSet):
    serializer_class = SocialMediaAccountSerializer
    queryset = SocialMediaAccount.objects.all()

