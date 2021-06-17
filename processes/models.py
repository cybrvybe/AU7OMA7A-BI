from django.db import models
from django.db.models.deletion import DO_NOTHING
from general_business.models import Organization
from content.models import AbstractModel
# Create your models here.
class Process(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name = "Process Title"
    )
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description",
        blank = True
    )
    #creates relationship with model "Organization" from "general_business" app.
    parent_organization = models.ManyToManyField(
        to = Organization,
        blank = True
    )
    subprocess = models.ManyToManyField(
        to = "processes.Process",
        blank = True,
        related_name = "+"
    )
 
    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.parent_organization}"


