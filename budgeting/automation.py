class FinancialSummary:

    def get_essential_recurring_expenses(expenses):
        essential_recurring_expenses = []
        for expense in expenses:
            if expense.is_recurring == True & expense.is_essential:
                essential_recurring_expenses.append(expense)
        return essential_recurring_expenses

    def normalize_recurring_freq_units(expenses):
        normalized_recurring_freq_unit_expenses = []
        for expense in expenses:
            #break down recurring freq into list
            recurring_freq = expense.recurring_freq
            recurring_freq_split = recurring_freq.split(' ')
            recurring_freq_unit = recurring_freq_split[1].lower()
            if recurring_freq_unit == "months":
                num_months = int(recurring_freq_split[0])
                num_weeks = num_months*4
                new_recurring_freq_split = [
                    str(num_weeks),
                    "weeks"
                ]
                new_recurring_freq = " ".join(new_recurring_freq_split)
                print("New Recurring Freq: " + new_recurring_freq)
                expense.recurring_freq = new_recurring_freq
            return expenses
            

#def get_essential_recurring_cost_of_living():
    
    #separate expenses by essential, recurring expenses.
 #   get_essential_recurring_expenses(expenses)

