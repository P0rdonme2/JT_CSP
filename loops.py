# JT Loops Notes
# 1:Start point
#2:Stop point boolean statement
#3:Increase iterater = vocab
# Iterater = keeping count of what you are doing
# Iteration = what you are doing
# Everything inside loop should be tabed in
# The last line of your while loop increase iterater
import random

count = 1
while count <= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break # Continue sends you back to the begining of the loop
    print("Duck. . . .")
    ducks += 1 # ducks = ducks+1
print("GOOSE!!!")

# Complex Data Type = holds other data in it
family = ["James", "Katie", "Jaxon"] # Every item must be valid data type, every item seperated by commas, surrounded by brackets
print(family[2])