from django.db import models
from general_business.models import Organization

# Create your models here.
#This class stores a business Project
class Project(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Project Title"

    )
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
    
    parent_organization = models.ForeignKey(
        to = Organization,
        verbose_name = "Parent Organization",
        on_delete=models.CASCADE,
        null = True,
        blank = True

    )
    def __str__(self):
        return f"{self.title}, {self.parent_organization}, {self.subtitle}"
