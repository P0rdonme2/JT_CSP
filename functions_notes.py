# JT Functions Notes 
def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"What is your monthly {money}:"))
            return amount
        except:
            print("That isn't a number :(")


# Write all your variables
income = stupid_proof('income')
rent =stupid_proof("rent")
utilities = stupid_proof("utilities")
groceries = stupid_proof("groceries")

transportation = stupid_proof("transportation")
savings = income * .1
# Write any functions you are using
# def means define
# calc_percent is the name of the functions no spaces
# Function a named group of programming instructions that can be reused any time you need them
# After variable name put perens
# Income and bill is the parameters which are peices of info needed for variable to run
# End it with a colon
# return is a print put not sending it to user but to code
# calc_percent(income,rent) is the function call the income and rent in that is the arguements
# parameter variable name agruement value for perameters when I call my function
# made for repetitive Code, Makes code easier to read, and break problems into smaller peices
def calc_percent(income, bill):
    return round(bill/income * 100)

# Outputs for the user
print(f"Your rent is ${rent:.2f} that is {calc_percent(income,rent)}% of your income")
print(f"You should save ${savings:.2f} that is {calc_percent(income,savings)}% of your income")
print(f"Your utilities is ${utilities:.2f} that is {calc_percent(income,utilities)}% of your income")
print(f"Your groceries is ${groceries:.2f} that is {calc_percent(income,groceries)}% of your income")
print(f"Your transportaion is ${transportation:.2f} that is {calc_percent(income,transportation)}% of your income")
print(f"You have ${income-rent-utilities-groceries-transportation-savings:.2f} left to spend")