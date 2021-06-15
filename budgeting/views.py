from django.shortcuts import render
from rest_framework import viewsets, serializers, views
from rest_framework.response import Response
from .serializers import BudgetSerializer, ExpenseSerializer, IncomeEventSerializer, IncomeStreamSerializer
from .models import Budget, Expense, IncomeEvent, IncomeStream

class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()

class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

class IncomeStreamView(viewsets.ModelViewSet):
    serializer_class = IncomeStreamSerializer
    queryset = IncomeStream.objects.all()

class IncomeEventView(viewsets.ModelViewSet):
    serializer_class = IncomeEventSerializer
    queryset = IncomeEvent.objects.all()








######################################################
#CALCULATION-BASED VIEWS
######################################################

class ExpenseTimeIntervalCostBreakdownView(views.APIView):
    def get(self, request):
        #Validates input data
        serializer = ExpenseSerializer(
            data = request.query_params
        )
        serializer.is_valid(raise_exception = True)

        #Get data requested by "query_params", in "request"/
        #  - which was fed to "serializer".
        expenses_jsons = serializer.validated_data
        #create empty lists to iterate and append to, after/
        # searching through "expenses_json" for the specified data.
        iteration_list = [
            {
                "value": "daily",
                "multiplier": 365.3333333
            },
            {
                "value": "weekly",
                "multiplier": 52.1429
            },
            {
                "value": "monthly",
                "multiplier": 12
            },
            {
                "value": "quarterly",
                "multiplier": 4
            },
            {
                "value": "biannual",
                "multiplier": 2
            },
            {
                "value": "annual",
                "multiplier": 1
            }
        ]
        total_annual_expenses = []
        for expense_json in expenses_jsons:
            for obj in iteration_list:
                if expense_json[obj["value"]] == "daily":
                    total_annual_amount = expense_json["amount"]*obj["multiplier"]
                    total_annual_expenses.append(total_annual_amount)
        total_annual_cost = sum(total_annual_expenses)
        total_daily_cost = total_annual_cost/365.3333
        total_weekly_cost = total_annual_cost/52.1429
        total_monthly_cost = total_annual_cost/12
        total_quarterly_cost = total_annual_cost/4
        total_biannual_cost = total_annual_cost/2
        
                

        return Response(
            {
                "title": "Time-Interval Based Expense Cost Calculation",
                "description": "Calculates the expense costs based on query_params, and separates that data into time-interval-based categories (daily, monthly, etc)",
                "daily": total_daily_cost,
                "weekly": total_weekly_cost,
                "monthly": total_monthly_cost,
                "quarterly": total_quarterly_cost,
                "biannual": total_biannual_cost,
                "annual": total_annual_cost
            }
        )

        
