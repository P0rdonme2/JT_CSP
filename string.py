# JT, String Notes

# string=> any saved inside of quotation marks " " ' '

name = input('What is your name: ').strip().capitalize()

age = input('How old are you:')
print(type(age))

# Concatenation => puts two strings directly next to each other
print(age+age)

print(name + ' ' + 'LaRose')
#
sentence = "The quick brown fox jumped over the lazy dog."
print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name)) #<= gets the length of a string
print(f"Your name is {name} that is {len(name)} letters long. Your first initial is {name[0]} I think I will call you {name[0:3]}")
# string.action/method()
# strip removes spaces from the begining and the end
# f-string=>formated string lets you write code inside your string
# len tells you the length of something
# index# is the specifice letter
#slice=>take a string pull out a smaller piece