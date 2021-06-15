from django.db import models
from content.models import AbstractDescModel

# Create your models here.
class Metric(AbstractDescModel):
    abbreviation = models.CharField(
        max_length = 50,
        null = True,
        blank = True
    )
    equation = models.CharField



