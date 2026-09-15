# JT Fixing user inputs

while True:
    color = input("Tell me a color that is only one word: ").strip().lower()
    if color.isnumeric():
        print("That is a number not a color!")
    elif " "in color:
          print("I said one word.")
    else:
        break

print(f"We painted the wals {color}!")