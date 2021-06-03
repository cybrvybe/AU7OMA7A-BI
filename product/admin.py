from django.contrib import admin
from .models import Feature, Product, Service
# Register your models here.
models = [
    Product,
    Service,
    Feature
]
for model in models: 
    admin.site.register(model)