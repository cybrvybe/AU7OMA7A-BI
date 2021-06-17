from processes.models import Process
from django.contrib import admin
from .models import Process
# Register your models here.
models = [
    Process
]
for model in models: 
    admin.site.register(model)