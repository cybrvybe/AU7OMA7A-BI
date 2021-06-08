from django.db import models

# Create your models here.
class Company(models.Model):
    title = models.CharField(
        max_length = 500,
        verbose_name = "What is the company name?"
    )
    page_url = models.URLField(
        null =True,
        blank = True,
        verbose_name = "Enter a URL to the company's website"
    )
    linked_in_url = models.URLField(
        null = True,
        blank = True,
        verbose_name = "Enter a URL to the company's LinkedIn page."
    )
    company_type = models.CharField(
        max_length = 300,
        verbose_name = "What is the company type (LLC, S-Corp, etc)?",
        null = True,
        blank = True
    )
    company_size = models.CharField(
        max_length = 300,
        verbose_name = "What is the company size (SME, Startup, Corporate Behemoth, etc)?",
        null = True,
        blank = True
    )
    employee_count = models.CharField(
        max_length = 300,
        verbose_name = "What is the company's employee count?",
        null = True,
        blank = True
    )

    def __str__(self):
        return f"{self.title}, {self.company_type}"
class CareerContact(models.Model):
    first_name = models.CharField(
        max_length = 300,
        verbose_name = "What is your contact's first name?",
        null = True,
        blank = True
    )
    alias = models.CharField(
        max_length = 300,
        verbose_name = "If your contact has one, what is their alias?",
        null = True,
        blank = True
    )
    last_name = models.CharField(
        max_length = 300,
        verbose_name = "What is your contact's last name?",
        null = True,
        blank = True
    )
    phone_number = models.IntegerField(
        null = True,
        blank = True
    )
    uploaded_at = models.DateTimeField(
        auto_now = True
    )
    email = models.EmailField(
        null = True,
        blank = True
    )
    gender = models.CharField(
        max_length = 500,
        null = True,
        blank = True,

    )
    parent_company = models.ForeignKey(
        to = Company,
        on_delete = models.DO_NOTHING,
        null = True,
        blank = True

    )
    def __str__(self):
        return f"{self.first_name}, {self.last_name}: {self.parent_company}"
class CareerRole(models.Model):
    title = models.CharField(
        max_length = 300,
        verbose_name = "What is the role title?"
    )
    parent_company = models.ForeignKey(
        to = Company,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )