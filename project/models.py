from django.db import models
from general_business.models import Organization
from product.models import Product, Service
from content.models import AbstractDescModel, AbstractModel
# Create your models here.
#This class stores a business Project
class Project(AbstractModel):

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
    parent_product = models.ForeignKey(
        to = Product,
        verbose_name = "Parent Product",
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.parent_organization}, {self.subtitle}"
class Feature(AbstractModel):
    
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
    subfeatures = models.ManyToManyField(
        to = "project.Feature",
        null = True,
        blank = True
    )
    description = models.CharField(
        max_length = 1000,
        null = True, 
        verbose_name = "Description",
        blank = True
    )
    parent_product = models.ForeignKey(
        to = Product,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    parent_service = models.ForeignKey(
        to = Service,
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )
    parent_project = models.ForeignKey(
        to = Project,
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )
    choices = (
        (
            "User-Facing Feature",
            "User-Facing Feature"
        ),
        (
            "Development Feature",
            "Development Feature"
        ),
        (
            "UI Design Feature",
            "UI Design Feature"
        )
    )
    feature_type = models.CharField(
        choices = choices,
        max_length = 400,
        null = True,
        blank = True
    )
    status_choices = [
        (
            "Inactive",
            "Inactive"
        ),
        (
            "In Progress",
            "In Progress"
        ),
        (
            "Active",
            "Active"
        )
    ]
    status = models.CharField(
        max_length = 500,
        null = True,
        blank = True,
        choices = status_choices
    )
    def __str__(self):
        return f"{self.title},{self.feature_type}"

class Task(AbstractDescModel):
    parent_feature = models.ForeignKey(
        to = Feature,
        blank = True,
        null = True,
        on_delete = models.DO_NOTHING
    )
    subtasks = models.ManyToManyField(
        to = "project.Task",
        null = True,
        blank = True,
        related_name = "subtask_relation"

    )
    previous_task = models.ForeignKey(
        to = "project.Task",
        on_delete = models.DO_NOTHING,
        null = True,
        blank = True,
        related_name = "previous_task_relation"
    )
    next_task = models.ForeignKey(
        to = "project.Task",
        on_delete = models.DO_NOTHING,
        null = True,
        blank = True,
        related_name = "next_task_relation"
    )
    status_choices = [
        (
            "Cold",
            "Cold"
        ),
        (
            "In Queue",
            "In Queue"
        ),
        (
            "In Progress",
            "In Progress"
        ),
        (
            "Complete",
            "Complete"
        )
    ]
    parent_project = models.ForeignKey(
        to = Project,
        null = True,
        blank = True,
        on_delete = models.DO_NOTHING
    )
    status = models.CharField(
        max_length = 500,
        null = True,
        blank = True,
        choices = status_choices
    )
    
class Tech(AbstractModel):
    parent_feature = models.ManyToManyField(
        to = Feature,
        null = True,
        blank = True
    )
    tech_category_choices = [
    
        (
            "Front-End",
            "Front-End"
        ),
        (
            "DevOps",
            "DevOps"
        ),
        (
            "Back-End",
            "Back-End"
        ),
        (
            "Testing",
            "Testing"
        ),
        (
            "Database",
            "Database"
        ),
        (
            "Data Science",
            "Data Science"
        )

    ]
    tech_category = models.CharField(
        max_length = 500,
        choices = tech_category_choices,
        null = True,
        blank = True
        )
    def __str__(self):
        return f"{self.title} | {self.parent_feature} | {self.tech_category}"