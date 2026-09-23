# JT Password Strength Checker


characters = False
uppercase = False
lowercase = False
number = False
symbol = False
password = input("what is your password:")
if len(password) >= 8
    characters = True
for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercas = True
    if letter.isnumeric():
        number = True
    if letter in "!?@#$%()[]<>":
        symbol = True
        
print(f"At least 8 characters:{characters}")

print(f"Has an uppercase letter: {uppercase}")

Has a lowercase letter:

Has a number:

Has a symbol:
