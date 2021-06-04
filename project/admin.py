from django.contrib import admin
from .models import Feature, Project
# Register your models here.
models = [
    Project,
    Feature
]
for model in models:
    admin.site.register(model)