from rest_framework import serializers
from .models import Feature, Project
class ProjectSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Project
        fields = (
            "title",
            "subtitle",
            "parent_organization",
            "parent_product"
        )
class FeatureSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Feature
        fields = (
            "title",
            "subtitle",
            "description",
            "parent_product",
            "parent_service",
            "parent_project"
        )