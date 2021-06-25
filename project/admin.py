from django.contrib import admin
from .models import Feature, Project, Task, Tech
# Register your models here.
models = [
    Project,
    Feature,
    Tech,
    Task
]
for model in models:
    admin.site.register(model)