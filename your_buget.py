income = float(input("What is your monthly income:"))

rent = float(input("What is your monthly rent/mortgage:"))

utilities = float(input("What is your monthly utilities:"))

groceries = float(input("What is your monthly groceries:"))

transportation = float(input("What is your monthly transportation:"))

savings = income * 0.10

rent_pct = (rent / income) * 100
utilities_pct = (utilities / income) * 100
groceries_pct = (groceries / income) * 100
transportation_pct = (transportation / income) * 100
savings_pct = (savings / income) * 100
spending_money = income - rent - utilities - groceries - transportation - savings

print(f"Your rent is $ {rent:.2f} and that is {round(rent_pct)} % of your income.")
print(f"Your utilities are $ {utilities:.2f} and that is {round(utilities_pct)} % of your income.")
print(f"Your groceries are $ {groceries:.2f} and that is {round(groceries_pct)} % of your income.")
print(f"Your transportation is $ {transportation:.2f} and that is {round(transportation_pct)} % of your income.")
print(f"You should save $ {savings:.2f} a month, that is {round(savings_pct)} % of your income.")
print(f"You have $ {spending_money:.2f} of spending money each month!")