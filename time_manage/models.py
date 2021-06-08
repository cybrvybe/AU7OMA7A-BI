from django.db import models
from project.models import Project
from content.models import AbstractModel
class DaySchedule(AbstractModel):
    purpose = models.CharField(
        max_length = 500,
        null = True,
        blank = True
    )
class TimeSession(AbstractModel):
    description = models.CharField(
        max_length = 500,
        null = True,
        blank = True
    )
    start_time = models.DateTimeField(
        auto_now = True
    )
    end_time = models.DateTimeField(
        auto_now = False
    )
    parent_project = models.ForeignKey(
        to = Project,
        on_delete = models.DO_NOTHING
    )
    parent_day_schedule = models.ForeignKey(
        to = DaySchedule,
        on_delete = models.DO_NOTHING
    )
    def __str__(self):
        return f"{self.title}: {self.parent_project}"


