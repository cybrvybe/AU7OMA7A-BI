from django.contrib import admin
from .models import Product, Service
# Register your models here.
models = [
    Product,
    Service
]
for model in models: 
    admin.site.register(model)