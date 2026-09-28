# JT Password Strength Checker


characters =False
uppercase = False
lowercase = False
number = False
symbol = False
password = input("what is your password:")
if len(password) >= 8:
    characters = True
for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if letter in "!?@#$%()[]<>":
        symbol = True
        
print(f"At least 8 characters:{characters}")

print(f"Has an uppercase letter: {uppercase}")

print(f"Has a lowercase letter:{lowercase}")

print(f"Has a number:{number}")

print(f"Has a symbol:{symbol}")
score = 0
if len(password) >= 8:
    score = 1
    if letter.isupper():
        score = 1
    if letter.islower():
        score = 1
    if letter.isnumeric():
        score = 1
    if letter in "!?@#$%()[]<>":
        score = 1

print(f"Your password strength is:{score}")