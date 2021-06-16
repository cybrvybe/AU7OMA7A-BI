
from django.db import models
from django.db.models.deletion import DO_NOTHING
from content.models import AbstractModel, AbstractDescModel
from general_business.models import Organization

class Product(AbstractModel):
    
    subtitle = models.CharField(
        max_length =500,
        null = True,
        blank = True
    )
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = DO_NOTHING
    )
class Service(AbstractModel):
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = DO_NOTHING
    )
class PriceObj(AbstractModel):
    amount  = models.IntegerField(
        null = True,
        blank = True
    )
    is_recurring = models.BooleanField(
        verbose_name = "Is the price a recurring amount?"
    )
    RECURRENCE_FREQ_CHOICES = (
        ("daily", "daily"),
        ("weekly", "weekly"),
        ("monthly", "monthly"),
        ("annually", "annually")
    )
    reccurence_freq = models.CharField(
        choices = RECURRENCE_FREQ_CHOICES,
        null = True,
        blank = True,
        max_length = 500

    )