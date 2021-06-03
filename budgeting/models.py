from django.db import models
from general_business.models import Organization, Role
from product.models import Product, Service
# Create your models here.
class Budget(models.Model):
    title = models.CharField(
        max_length = 250,
        verbose_name = "Budget Title"
    )
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
class Expense(models.Model):
    title = models.CharField(
        max_length = 250,
        verbose_name = "Expense Title",

    )
    subtitle = models.CharField(
        max_length = 300,
        verbose_name = "Short Description",
        null = True,
        blank = True
    )
    parent_budget = models.ForeignKey(
        to = Budget,
        on_delete = models.CASCADE
    )
    cost = models.FloatField(
        verbose_name = "Cost ($)",
        null = True,
        blank = True,
    )
    is_recurring = models.BooleanField(
        verbose_name = "Is this payment recurring?"
    )
    recurrence_freq = models.CharField(
        verbose_name = "What is the recurrence frequency of this payment? (x weeks, x months, x years)",
        max_length = 300,
        blank = True,
        null = True
    )
    is_prospective = models.BooleanField(
        verbose_name = "Is this payment prospective?"   
    )
    is_business_expense = models.BooleanField(
        verbose_name = "Is this a business expense?"
    )
    is_asset = models.BooleanField(
        verbose_name = "Is this an asset?"
    )
    def __str__(self):
        return f"{self.title}, {self.subtitle}: ${self.cost} every {self.recurrence_freq}"

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
class IncomeEvent(models.Model):
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    amount = models.FloatField(
        verbose_name = "Income Amount ($)"
    )
    parent_income_stream = models.ForeignKey(
        to = IncomeStream,
        on_delete = models.CASCADE
    )
    is_recurring = models.BooleanField(
        verbose_name = "Is this income event recurring?"
    )
    recurrence_freq = models.CharField(
        max_length = 300,
        verbose_name = "What is the recurrence frequency of this income event in x weeks, months, or years?"
    )

    def __str__(self):
        return f"${self.amount}, {self.uploaded_at} // {self.parent_income_stream}"