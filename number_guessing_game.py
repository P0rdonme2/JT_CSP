# JT Number Guessing Game


import random


Mininum_Number= 1
Maximum_Number = 100


Max_Attempts = 6


secret_number = random.randint(Mininum_Number,Maximum_Number )

print(f"I'm thinking of a number between {Mininum_Number} and {Maximum_Number}. You have {Max_Attempts} tries to guess it!")

won = False
for attempt in range(1, Max_Attempts + 1):
    guess = int(input(f"Guess #{attempt}: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempt} tries!")
        won = True
        break 
if not won:
    print(f"You're out of guesses! The number was {secret_number}.")
