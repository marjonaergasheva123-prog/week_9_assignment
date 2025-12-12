transaction_list = [
    "01-Oct/Food/15.50",
    "02-Oct/Gas/40.00",
    "03-Oct/Food/12.25",
    "04-Oct/Rent/800.00",
    "05-Oct/Gas/35.00",
    "05-Oct/Food/8.75"
]
def group_expenses(transaction_list):
    expense_dict={}
    for item in transaction_list:
      data, category, cost=item.split('/')
      cost_new=float(cost)
      if category in expense_dict:
        expense_dict[category].append((data,cost_new))
      else:
        expense_dict[category]=[(data,cost_new)]
        
    return expense_dict

expense_dict = group_expenses(transaction_list)

def summarize_budget(expense_dict):
    for category, list_of_tuples in expense_dict.items():
        total=0
        for data,cost in list_of_tuples:
           total+=cost
        print(f"  {category}:  ${total:.2f} total")


summarize_budget(expense_dict)










