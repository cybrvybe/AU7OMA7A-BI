from processes.models import Process
from django.contrib import admin
from .models import Process, AlgoUnit
# Register your models here.
models = [
    Process,
    AlgoUnit
]
for model in models: 
    admin.site.register(model)