from project.models import Project
from django.db import models
from general_business.models import Organization
from project.models import Project

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Product Title",
        null = True
    )
    subtitle = models.CharField(
        max_length = 300,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.parent_organization}"
class Service(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Service Title",
        blank = True,
        null = True
    )
    is_recurring = models.BooleanField(
        verbose_name = "Is this service recurring?",
    
    )
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"

class Feature(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Feature Title"
    )
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description",
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
    def __str__(self):
        return f"{self.title},{self.subtitle}"

