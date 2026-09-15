# AB, 15/9/2026 Hello User Assingment.

# what is your name

# print hello name while loop
while True:
    name = input("What is your name???").strip().title()
    if name.isnumeric():
        print("Dude. No numbers.")
    elif " " in name:
        print(f"Gonna be formal eh? My most humble greetings {name}.")
    else:
        break
print(f"Hello {name}.")
