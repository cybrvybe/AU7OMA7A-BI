
from rest_framework import serializers
from .models import InstagramCarousel, InstagramCarouselPage, Story, Tweet, TwitterThread, VideoContent

class InstagramCarouselSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = InstagramCarousel
        fields = (
            "title",
            "created_at",
            "png_file",
            "svg_file",
            "count"
        )
class InstagramCarouselPageSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = InstagramCarouselPage
        fields = (
            "title",
            "created_at",
            "png_file",
            "svg_file",
            "parent_carousel"
        )
class StorySerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Story
        fields = (
            "title",
            "created_at",
            "content_file",
            "poll_question",
            "social_account"
        )
class TwitterThreadSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = TwitterThread
        fields = (
            "title",
            "created_at"
        )
class TweetSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Tweet
        fields = (
            "title",
            "created_at",
            "img_file",
            "content_text",
            "date_uploaded",
            "parent_thread"
        )
class VideoContentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = VideoContent
        fields = (
            "title",
            "created_at",
            "video_file",
            "subtitle_transcription",
            "type"
        )