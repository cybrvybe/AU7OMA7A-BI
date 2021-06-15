from django.db.models.deletion import DO_NOTHING
from content.models import AbstractDescModel
from django.db import models
from content.models import AbstractDescModel
from modules.models import Module
from metrics.models import Metric

# Create your models here

class AutonomousAnalysis(AbstractDescModel):
    function_class_name = models.CharField(
        verbose_name = "What is the class name of the corresponding view?",
        null = True,
        blank = True,
        max_length = 500
    )
    parent_module = models.ForeignKey(
        to = Module,
        on_delete = DO_NOTHING,
        null = True,
        blank = True
    )
    metrics = models.ManyToManyField(
        to = Metric,
        blank = True
    )

    def __str__(self):
        return f"{self.title} ({self.parent_module})"