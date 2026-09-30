# JT Caesar Cipher
# Make variables
# Make a for loop
# in your loop make a conditional that tells if it is a letter and if you print it out
# Use the number the user gave you to increase your letter
#Chek to make sure the if you have went over the alphebet
# add letter to a variable with an empty string
# build decripture change the users number to a negative

choice = input("Would you like to Encrypt or Decrypt a message:")
message = input ("Enter your message:")
shift = int(input("Enter a shift amount:"))
finished = ""
for letter in message:

    if letter .isalpha():
        scrambeled = ord(letter)+ shift
        
    if scrambeled > 90 and letter.isupper():
        scrambeled -= 26
    if scrambeled > 122 and letter.islower():
        scrambeled -= 26
    finished+= chr(scrambeled)
    
print(finished)