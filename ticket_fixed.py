#AB fixed ticket code

while True:
    try:
        age = int(input("Enter your age: "))
        age = int(age)
        if age < 5:
            price = 0
        elif age <= 12:
            price = 8
        elif age < 65:
            price = 12
        else:
            print("Invalid age.")
            break
        matinee = input("Is this a matinee? (yes/no): ").lower().strip()
        if matinee == "yes":
                price = price - 3
        elif matinee == "no":
             pass

        print(f"Ticket price: ${price}")
        break
    except:
        print("Invalid input. Please enter a matinee input of 'yes' or 'no'.")