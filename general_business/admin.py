from django.contrib import admin
from .models import AlgoUnit, Campaign, Feature, Organization, Process, Product, Project, Role, Service, Venture
# Register your models here.
models = [
    Organization,
    Process,
    AlgoUnit,
    Venture,
    Product,
    Service,
    Campaign,
    Role,
    Feature,
    Project
]
for model in models: 
    admin.site.register(model)