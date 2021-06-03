from django.db import models
from general_business.models import Organization
# Create your models here.
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
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}, {self.parent_organization}"
# Create your models here.
class Brand(models.Model):
    logo_svg = models.ImageField(
        verbose_name = "SVG file of logo",
        null = True,
        blank = True
    )
    mantra = models.CharField(
        max_length = 250,
        verbose_name = "Brand Mantra",
        null = True,
        blank = True
    )
    colors = models.JSONField(
        verbose_name = "Store brand colors in JSON format.",
        null = True,
        blank = True
    )
    logo_mockup = models.ImageField(
        verbose_name = "Enter a logo mockup image"
    )
    topic_keywords = models.CharField(
        verbose_name = "Enter keywords describing your brand, separated by commas.",
        max_length = 10000
    )
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE
    )

class SocialMediaAccount(models.Model):
    social_medium = models.CharField(
        max_length = 300,
        verbose_name = "What is the social medium of this social media account?"
    )
    username = models.CharField(
        max_length = 300,
        verbose_name = "What is the username of this social media account?"
    )
    password = models.CharField(
        max_length = 300,
        verbose_name = "What is the password of this social media account?"
    )
    purpose = models.CharField(
        max_length = 500,
        verbose_name = "What is the purpose of this social media account?",


    )
    parent_brand = models.ForeignKey(
        to = Brand,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    page_url = models.URLField(
        verbose_name = "Enter social media page URL."
    )
    def __str__(self):
        return f"{self.username}: {self.social_medium}"