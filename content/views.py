from django.db.models import query
from django.shortcuts import render
from .models import InstagramCarouselPage, Story, InstagramCarousel, TwitterThread, Tweet, VideoContent
from .serializers import InstagramCarouselPageSerializer, InstagramCarouselSerializer, StorySerializer, TweetSerializer, TwitterThreadSerializer, VideoContentSerializer
from rest_framework import viewsets

#generic model api views
class StoryView(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()
class InstagramCarouselView(viewsets.ModelViewSet):
    serializer_class = InstagramCarouselSerializer
    queryset = InstagramCarousel.objects.all()
class InstagramCarouselPageView(viewsets.ModelViewSet):
    serializer_class = InstagramCarouselPageSerializer
    queryset = InstagramCarouselPage.objects.all()
class TwitterThreadView(viewsets.ModelViewSet):
    serializer_class = TwitterThreadSerializer
    queryset = TwitterThread.objects.all()
class TweetView(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
class VideoContentView(viewsets.ModelViewSet):
    serializer_class = VideoContentSerializer
    queryset = VideoContent.objects.all()