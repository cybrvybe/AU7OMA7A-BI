from rest_framework import serializers
from .models import Brand, Campaign, SocialMediaAccount

class CampaignSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Campaign
        fields = (
            "title",
            "subtitle",
            "uploaded_at",
            "parent_organization"
        )
class BrandSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Brand
        fields = (
            "logo_svg",
            "mantra",
            "colors",
            "logo_mockup",
            "topic_keywords",
            "parent_organization"
        )
class SocialMediaAccountSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = SocialMediaAccount
        fields = (
            "social_medium",
            "username",
            "password",
            "purpose",
            "parent_brand",
            "page_url"
        )