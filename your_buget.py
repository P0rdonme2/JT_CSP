income = float(input("What is your monthly income:"))

rent = float(input("What is your monthly rent/mortgage:"))

utilities = float(input("What is your monthly utilities:"))

groceries = float(input("What is your monthly groceries:"))

transportation = float(input("What is your monthly transportation:"))

saving = income * 0.10

print((f"Your rent is {rent:.2f} and that is {int(rent/ income * 100)}% of your income."))

print(f"Your utilities is {utilities:.2f} and that is {int(utilities/income * 100)}% of your income.")

print(f"Your groceries is {groceries:.2f} and that is {int(groceries/income * 100)}% of your income.")

print(f"Your transportation is {transportation:.2f} and that is {int(transportation/income * 100)}% of your income.")
spending = (income - rent) + (income - utilities) + (income - groceries) + (income - transportation)
print(f"You should save {saving} a month, that is  of your income.")
print(f"You have {spending} of spending money each month!") 