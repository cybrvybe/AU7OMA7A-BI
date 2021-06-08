from django.db.models import query
from django.shortcuts import render
from .models import InstagramCarouselPage, Story, InstagramCarousel, TwitterThread, Tweet
from .serializers import InstagramCarouselSerializer, StorySerializer
from rest_framework import viewsets

#generic model api views
class StoryView(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()
class InstagramCarouselView(viewsets.ModelViewSet):
    serializer_class = InstagramCarouselSerializer
    queryset = InstagramCarousel.objects.all()
class InstagramCarouselPageView(viewsets.ModelViewSet):
    serializer_class = InstagramCarouselPage
    queryset = InstagramCarouselPage.objects.all()
class TwitterThreadView(viewsets.ModelViewSet):
    serializer_class = TwitterThread
    queryset = TwitterThread.objects.all()
class Tweet(viewsets.ModelViewSet):
    serializer_class = Tweet
    queryset = Tweet.objects.all()