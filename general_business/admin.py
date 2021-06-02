from django.contrib import admin
from .models import AlgoUnit, Campaign, Organization, Process, Product, Role, Service, Venture
# Register your models here.
models = [
    Organization,
    Process,
    AlgoUnit,
    Venture,
    Product,
    Service,
    Campaign,
    Role
]
for model in models: 
    admin.site.register(model)