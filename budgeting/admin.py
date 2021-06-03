from django.contrib import admin
from .models import Budget, Expense
# Register your models here.

models = [
    Budget,
    Expense
]
for model in models: 
    admin.site.register(model)