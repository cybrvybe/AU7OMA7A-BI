from analytics.models import AutonomousAnalysis
from django.contrib import admin
from .models import AutonomousAnalysis
models = [
    AutonomousAnalysis
]
# Register your models here.
for model in models:
    admin.site.register(model)