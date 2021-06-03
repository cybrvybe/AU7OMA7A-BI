from django.contrib import admin
from .models import Organization, Role, Venture
# Register your models here.
models = [
    Organization,
    Venture,
    Role
]
  
for model in models: 
    admin.site.register(model)