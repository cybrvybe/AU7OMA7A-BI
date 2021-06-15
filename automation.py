import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_dir.settings')
django.setup()
application = get_wsgi_application()
from budgeting.models import Expense, IncomeEvent, Budget
 
class BudgetingAutomation:
    expenses = Expense.objects.all()
    recurring_expenses = Expense.objects.filter(is_recurring = True)
    asset_expenses = Expense.objects.filter(is_asset = True)
    recurring_yearly_expenses = Expense.objects.filter(
        is_recurring = True,
        recurrence_freq = "1 year"
    )
    recurring_monthly_expenses = Expense.objects.filter(
        is_recurring = True, 
        recurrence_freq = "1 month"
    )
    recurring_weekly_expenses = Expense.objects.filter(
        is_recurring = True, 
        recurrence_freq = "1 week"
    )
    recurring_daily_expenses = Expense.objects.filter(
        is_recurring = True,
        recurrence_freq = "1 day"
    )
    #lower-level functions
    ###########################

    #
    def get_expense_amounts_list(expenses):
        expense_amounts = []
        for expense in expenses:
            amount = expense.amount
            expense_amounts.append(amount)
        return expense_amounts
    def get_total_expense_amount(expense_amounts):
       total_expense_amount = sum(expense_amounts)
       return total_expense_amount 


    #gets the list of all expense amounts.
    all_expense_amounts_list = get_expense_amounts_list(expenses)
    
    recurring_expense_amounts_list = get_expense_amounts_list(recurring_expenses)
    daily_recurring_expense_amounts_list = get_expense_amounts_list(recurring_daily_expenses)
    weekly_recurring_expense_amounts_list = get_expense_amounts_list(recurring_weekly_expenses)
    monthly_recurring_expense_amounts_list = get_expense_amounts_list(recurring_monthly_expenses)
    yearly_recurring_expense_amounts_list = get_expense_amounts_list(recurring_yearly_expenses)
    recurring_expenses_lists_dict = {
        "daily": daily_recurring_expense_amounts_list,
        "weekly": weekly_recurring_expense_amounts_list,
        "monthly": monthly_recurring_expense_amounts_list,
        "yearly": yearly_recurring_expense_amounts_list
    }

    def get_required_recurring_income(recurrence_interval, recurring_expenses_lists_dict):
        daily_expenses = recurring_expenses_lists_dict["daily"]
        weekly_expenses = recurring_expenses_lists_dict["weekly"]
        monthly_expenses = recurring_expenses_lists_dict["monthly"]
        yearly_expenses = recurring_expenses_lists_dict["yearly"]

        daily_expenses_sum = sum(daily_expenses)
        weekly_expenses_sum = sum(weekly_expenses)
        monthly_expenses_sum = sum(monthly_expenses)
        yearly_expenses_sum = sum(yearly_expenses)

        total_yearly_expenses = (daily_expenses_sum*365.333) + (weekly_expenses_sum*52.1429) + (monthly_expenses_sum*12) + (yearly_expenses_sum)


        if recurrence_interval == "daily":
            req_daily_recurring_income = total_yearly_expenses/365.333
            print("$" + str(req_daily_recurring_income) + " per day")
            return req_daily_recurring_income
        if recurrence_interval == "weekly":
            req_weekly_recurring_income = total_yearly_expenses/52.1429
            print("$" + str(req_weekly_recurring_income) + " per week")
            return req_weekly_recurring_income
        if recurrence_interval == "monthly": 
            req_monthly_recurring_income = total_yearly_expenses/12
            print("$" + str(req_monthly_recurring_income) + " per month")
            return req_monthly_recurring_income
        if recurrence_interval == "yearly":
            print("$" + str(total_yearly_expenses) + " per year")
            return total_yearly_expenses


    ###############################################
    ###########################################
    ######Income Management
    ################################################
    #################################################
    income_events = IncomeEvent.objects.all()
    recurring_income_events = IncomeEvent.objects.filter(is_recurring = True)
    recurring_daily_income_events = IncomeEvent.objects.filter(
        is_recurring = True,
        recurrence_freq = "1 day"
    )
    recurring_weekly_income_events = IncomeEvent.objects.filter(
        is_recurring = True,
        recurrence_freq = "1 week"
    )
    recurring_monthly_income_events = IncomeEvent.objects.filter(
        is_recurring = True,
        recurrence_freq = "1 month"
    )
    recurring_yearly_income_events = IncomeEvent.objects.filter(
        is_recurring = True,
        recurrence_freq = "1 year"
    )
    def get_annual_income(self):
        
        recurring_daily_income_amounts = []
        for daily_income_event in self.recurring_daily_income_events:
            recurring_daily_income_amounts.append(daily_income_event.amount*365.3333)
        recurring_daily_income_amount_annual_sum = sum(recurring_daily_income_amounts)

        recurring_weekly_income_amounts = []
        for weekly_income_event in self.recurring_weekly_income_events:
            recurring_weekly_income_amounts.append(weekly_income_event.amount*52.1429)
        recurring_weekly_income_amount_annual_sum = sum(recurring_weekly_income_amounts)

        recurring_monthly_income_amounts = []
        for monthly_income_event in self.recurring_monthly_income_events:
            recurring_monthly_income_amounts.append(monthly_income_event.amount*12)
        recurring_monthly_income_amount_annual_sum = sum(recurring_monthly_income_amounts)

        recurring_yearly_income_amounts = []
        for yearly_income_event in self.recurring_yearly_income_events:
            recurring_yearly_income_amounts.append(yearly_income_event.amount)
        recurring_yearly_income_amount_annual_sum = sum(recurring_yearly_income_amounts)

        income_sums = [
            recurring_daily_income_amount_annual_sum,
            recurring_weekly_income_amount_annual_sum,
            recurring_monthly_income_amount_annual_sum,
            recurring_yearly_income_amount_annual_sum
        ]
        total_annual_sum = sum(income_sums)
        return total_annual_sum
    def get_income_by_time_interval(total_annual_income, time_interval):
        
        if time_interval == "daily":
            daily_income = total_annual_income/365.33333
            return daily_income
        if time_interval == "weekly":
            weekly_income = total_annual_income/52.1429
            return weekly_income
        if time_interval == "monthly":
            monthly_income = total_annual_income/12
            return monthly_income
        if time_interval == "yearly": 
            return total_annual_income
    def show_all_income_by_time_interval(self, annual_income):

        print_objs = [
            "-------------------------------------------",
            "Income by Time Interval:",
            "-------------------------------------------",
            "Daily: $" + str(self.get_income_by_time_interval(
                time_interval = "daily",
                total_annual_income = annual_income
                )
            ),
            "Weekly: $" + str(self.get_income_by_time_interval(
                time_interval = "weekly",
                total_annual_income = annual_income#self.get_annual_income(self)
                )
            ),
            "Monthly: $" + str(self.get_income_by_time_interval(
                time_interval = "monthly",
                total_annual_income = annual_income#self.get_annual_income(self)
                )
            ),
            "Yearly: $" + str(self.get_income_by_time_interval(
                time_interval = "yearly",
                total_annual_income = annual_income
                )
            )
        ]
        for obj in print_objs:
            print(obj)

        

        

            

def master():
    print_objs = [
        "______________________________________________",
        "AU7OMA7A-BI: All Expenses",
        "______________________________________________",
        BudgetingAutomation.all_expense_amounts_list,
        "______________________________________________",
        "AU7OMA7A-BI: Recurring Expenses",
        "______________________________________________",
        BudgetingAutomation.recurring_expense_amounts_list,
        "______________________________________________",
        "AU7OMA7A-BI: Required Recurring Expenses",
        "______________________________________________",
        "Daily: $"+ str(BudgetingAutomation.get_required_recurring_income(
            "daily", 
            BudgetingAutomation.recurring_expenses_lists_dict
        )),
        "Weekly: $" + str(BudgetingAutomation.get_required_recurring_income(
            "weekly", 
            BudgetingAutomation.recurring_expenses_lists_dict
        )),
        "Monthly: $" + str(BudgetingAutomation.get_required_recurring_income(
            "monthly", 
            BudgetingAutomation.recurring_expenses_lists_dict
        )),
        "Yearly: $" + str(BudgetingAutomation.get_required_recurring_income(
            "yearly", 
            BudgetingAutomation.recurring_expenses_lists_dict
        ))

    ]
    for print_obj in print_objs:
        print(print_obj)
    BudgetingAutomation.show_all_income_by_time_interval(
        self = BudgetingAutomation,
        annual_income = BudgetingAutomation.get_annual_income(self = BudgetingAutomation))
master()
    



    


