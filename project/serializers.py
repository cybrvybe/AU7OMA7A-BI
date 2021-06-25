from rest_framework import serializers
from .models import Feature, Project, Task, Tech
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
            "parent_project",
            "subfeatures"
        )
class TechSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Tech
        fields = (
            "title",
            "created_at",
            "tech_Category",
            "parent_feature"
        )
class TaskSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Task
        fields = (
            "title",
            "created_at",
            "parent_feature",
            "subtask",
            "previous_task",
            "next_task"
        )