from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Campaign
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )