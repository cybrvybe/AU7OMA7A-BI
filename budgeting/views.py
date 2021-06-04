from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BudgetSerializer, ExpenseSerializer
from .models import Budget, Expense, IncomeEvent, IncomeStream
# Create your views here.

class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()

class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

class IncomeStreamView(viewsets.ModelViewSet):
    serializer_class = IncomeStream
    queryset = IncomeStream.objects.all()

class IncomeEventView(viewsets.ModelViewSet):
    serializer_class = IncomeEvent
    queryset = IncomeEvent.objects.all()

    