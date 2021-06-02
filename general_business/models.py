from django.db import models

# Create your models here.
class Organization(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Business Name"
    )
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description"
    )
    parent_organization = models.ForeignKey(
        to = "general_business.Organization",
        null = True,
        verbose_name = "Parent Organization",
        on_delete=models.CASCADE,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"
#This class stores business ventures 
class Venture(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Venture Title"
    )
    subtitle = models.CharField(
        max_length = 300,
        verbose_name = "Short Description"
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"
class Product(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Product Title",
        null = True
    )
    subtitle = models.CharField(
        max_length = 300,
        verbose_name = "Short Description"
    )
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"
class Service(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Service Title"
    )
    is_recurring = models.BooleanField(
        verbose_name = "Is this service recurring?"
    )
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"
class Campaign(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Campaign Title"
    )
    subtitle = models.CharField(
        max_length=300,
        verbose_name="Short Description"
    )
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}"
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
        return f"{self.title}, {self.subtitle}"
class Role(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name = "Role Title"
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
        return f"{self.title}, {self.subtitle}"
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


