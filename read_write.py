# JT Reading and Writing to Files



# with open = function
# practice.txt = file path
# r = what we do with this file also read
# as file = name of file in the code
with open("practice.txt", "r+") as file: # r+ = read and appending
    #read gives what is written on the file
    content = file.read()
    content = "Chapter 1:\n" + content + " And Christopher Robin was sitting on his doorstep putting on his big boots."
    file.write(content)

# w = write 
# write = replaces content
# a = appened 
# appened = add content to the end
with open("practice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day")
