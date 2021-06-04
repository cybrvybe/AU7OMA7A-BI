from django.db import models

#An "Organization" represents a a business organization or company. Can represent a career as well.
class Organization(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Business Name",
        null = True,
        blank = True
    )
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description",
        null = True,
        blank = True
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
#This class stores business ventures (~mid-term goals)
class Venture(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Venture Title",
        null = True,
        blank = True
    )
    subtitle = models.CharField(
        max_length = 300,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.parent_organization}"


class Role(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name = "Role Title",
        null = True,
        blank = True
    )
    subtitle = models.CharField(
        max_length = 500,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
    #creates relationship with model "Organization" from "general_business" app.
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.parent_organization}"

