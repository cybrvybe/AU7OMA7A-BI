from rest_framework import serializers
from .models import TimeSession, DaySchedule

class TimeSessionSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = TimeSession
        fields = (
            "title",
            "created_at",
            "description",
            "start_time",
            "end_time",
            "parent_project",
            "parent_day_schedule"
        )
class DayScheduleSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = DaySchedule
        fields = (
            "title",
            "created_at",
            "purpose"
        )
