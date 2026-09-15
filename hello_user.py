# JT Hello user

while True:
    name = input("Tell me your first name:").strip().capitalize()
    if name.isnumeric():
        print("I said your name!")
    elif " " in name:
        print("I said your first name!")
    else:
        break

print(f"Hello {name}!!!!")