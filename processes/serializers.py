from rest_framework import serializers
from .models import Process, AlgoUnit
class ProcessSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Process
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
class AlgoUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoUnit
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )   