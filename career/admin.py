from django.contrib import admin
from .models import Company, CareerContact, CareerRole
# Register your models here.
models = [
    CareerRole,
    Company,
    CareerContact
]
for model in models:
    admin.site.register(model)