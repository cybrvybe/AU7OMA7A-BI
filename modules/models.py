from django.db import models
from content.models import AbstractModel
# Create your models here.

class Module(AbstractModel):
    purpose = models.CharField(
        max_length = 500,
        null = True,
        blank = True

    )
    
