from rest_framework import serializers
from .models import Budget, Expense, IncomeStream
class BudgetSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Budget
        fields = (
            'title',
            "parent_organization",
            "parent_product",
            "parent_service"
        )
        
class ExpenseSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Expense,
        fields = (
            "title",
            "subtitle",
            "parent_budget",
            "cost",
            "is_recurring",
            "recurrence_freq",
            "is_prospective",
            "is_business_expense",
            "is_asset",
            "is_essential"
        )

class IncomeStreamSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = IncomeStream
        fields = (
            "title",
            "parent_organization",
            "parent_product",
            "parent_service",
            "parent_role"
        )

class IncomeEventSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = IncomeStream
        fields = (
            "uploaded_at",
            "amount",
            "parent_income_stream",
            "is_recurring",
            "recurrence_freq"
        )