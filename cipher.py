# JT Caesar Cipher
# Make variables
# Make a for loop
# in your loop make a conditional that tells if it is a letter and if you print it out
# Use the number the user gave you to increase your letter
#Chek to make sure the if you have went over the alphebet
# add letter to a variable with an empty string
# build decripture change the users number to a negative

choice = input("Would you like to (E)ncrypt or (D)ecrypt a message:")
message = input ("Enter your message:")
shift = int(input("Enter a shift amount:"))


def cipher(message, shift):
    finished = ""
    for letter in message:
        if letter .isalpha():
            if letter.isupper():
                scrambeled = (ord(letter) - ord("A")+ shift) % 26 + ord("A") 
            else:
                scrambeled = (ord(letter) - ord("a") + shift) % 26 + ord("a")
            
        
        
        finished += chr(scrambeled)
    else:
        finished += letter

    return finished

    if choice.upper() == "D":
        shift = -shift

result = cipher(message, shift)

if choice.upper() == "E":
     print("Your encrypted message is:", result)
else:
     print("Your decrypted message is:", result)

