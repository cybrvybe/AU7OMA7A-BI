from django.contrib import admin
from .models import Budget, Expense, IncomeEvent, IncomeStream
# Register your models here.

models = [
    Budget,
    Expense,
    IncomeStream,
    IncomeEvent
]
for model in models: 
    admin.site.register(model)