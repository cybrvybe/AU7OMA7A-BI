from django.db import models
from general_business.models import Organization
# Create your models here.
class Process(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name = "Process Title"
    ),
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description"
    )
    #creates relationship with model "Organization" from "general_business" app.
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.parent_organization}"

#AlgoUnit: An AlgoUnit is short for "Algorithm Unit".
#It is a model of a step in a process.
class AlgoUnit(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Step Title",
    )
    parent_process = models.ForeignKey(
        to = Process,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"
    #create function to calculate step index of algounit
