from django.contrib import admin
from .models import Project
# Register your models here.
models = [
    Project
]
for model in models:
    admin.site.register(model)