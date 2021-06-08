from django.db import models
from general_business.models import Organization
from product.models import Product, Service
from content.models import AbstractModel
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

