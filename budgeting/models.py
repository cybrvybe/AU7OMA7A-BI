from django.db import models
from general_business.models import Organization, Role
from product.models import Product, Service
from content.models import AbstractModel
# Create your models here.
class AbstractFinEvent(AbstractModel):
    amount = models.FloatField(
        verbose_name = "Amount ($)",
        null = True,
        blank = True,
        default = 0
    )
   
class Budget(AbstractModel):
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    parent_product = models.ForeignKey(
        to = Product,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    parent_service = models.ForeignKey(
        to = Service,
        blank = True,
        null = True,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return f"{self.title}, {self.parent_organization}"
class AbstractBudgetItem(AbstractFinEvent):
    parent_budget = models.ForeignKey(
        to = Budget,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    is_prospective = models.BooleanField(
        default = True,
        null = True,
        blank = True
    )
    live_datetime = models.DateTimeField(
        auto_now = False,
        blank = True,
        null = True
    )
    subtitle = models.CharField(
        max_length = 300,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
class Expense(AbstractBudgetItem):
  
    is_recurring = models.BooleanField(
        verbose_name = "Is this payment recurring?"
    )
    RECURRENCE_FREQ_CHOICES = [
        ("daily","daily"),
        ("monthly", "monthly"),
        ("quarterly","quarterly"),
        ("biannual","biannual"),
        ("annual", "annual")
    ]
    recurrence_freq = models.CharField(
        verbose_name = "What is the recurrence frequency of this payment? (x weeks, x months, x years)",
        max_length = 300,
        blank = True,
        null = True,
        choices = RECURRENCE_FREQ_CHOICES
    )
    
    is_business_expense = models.BooleanField(
        verbose_name = "Is this a business expense?",
        null = True,
        blank = True
    )
    is_asset = models.BooleanField(
        verbose_name = "Is this an asset?",
        null = True,
        blank = True
    )
    is_essential = models.BooleanField(
        verbose_name = "Is this expense essential?",
        null = True,
        blank = True
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}: ${self.amount} every {self.recurrence_freq}"

class IncomeStream(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "Income Source Title",
        null = True,
        blank = True
    )
    parent_organization = models.ForeignKey(
        to = Organization,
        on_delete = models.CASCADE, 
        blank = True,
        null = True
    )
    parent_product = models.ForeignKey(
        to = Product,
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )
    parent_service = models.ForeignKey(
        to = Service,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    parent_role = models.ForeignKey(
        to = Role,
        on_delete = models.CASCADE,
        blank = True,
        null = True

    )
    def __str__(self):
        return f"{self.title}: {self.parent_organization}"
class IncomeEvent(AbstractFinEvent):
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    parent_income_stream = models.ForeignKey(
        to = IncomeStream,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    is_recurring = models.BooleanField(
        verbose_name = "Is this income event recurring?"
    )
    recurrence_freq = models.CharField(
        max_length = 300,
        verbose_name = "What is the recurrence frequency of this income event in x weeks, months, or years?",
        null = True,
        blank = True
    )
    is_prospective = models.BooleanField(
        verbose_name = "Is this a future income event?",
        null = True,
        blank = True
    )

    def __str__(self):
        return f"${self.amount} every {self.recurrence_freq}, {self.title} // IS RECURRING: {self.is_recurring}"