from metrics.models import Metric
from django.contrib import admin
from .models import Metric

models = [
    Metric
]
# Register your models here.
for model in models:
    admin.site.register(model)