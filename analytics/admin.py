from analytics.models import Bot
from django.contrib import admin
from .models import Bot
models = [
    Bot
]
# Register your models here.
for model in models:
    admin.site.register(model)