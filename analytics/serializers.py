from rest_framework import serializers
from .models import AutonomousAnalysis

class AutonomousAnalysisSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = AutonomousAnalysis
        fields = (
            "title",
            "description",
            "function_class_name"
        )