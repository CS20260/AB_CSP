# AB, 28/9/2026, Number Information

## instructions ##
    # Use a for loop to go through the numbers 1 through 20
    # Inside the loop, use a conditional to check if the number is even or odd
    # Nested inside that conditional, check whether the number is also divisible by 5
    # Print one message per number that reflects both checks (there should be 4 possible message types: even & divisible by 5, even & not divisible by 5, odd & divisible by 5, odd & not divisible by 5)


count = 1
for num in range(1,21):
    if num % 2 == 0:
        number = (f"{num} is even and not divisible by 5")
        if num % 5 == 0:
            number = (f"{num} is even and divisible by 5")
        else:
            number = (f"{num} is even and not divisible by 5")
    else:
        number = (f"{num} is odd and not divisible by 5")
        if num % 5 == 0:
            number = (f"{num} is odd and divisible by 5")
        else:
            number = (f"{num} is odd and not divisible by 5")
    print(number)
    