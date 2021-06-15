from django.contrib import admin
from .models import Module
models = [
    Module
]
# Register your models here.
for model in models:
    admin.site.register(model)