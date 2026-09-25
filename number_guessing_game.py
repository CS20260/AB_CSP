# AB, 25/9/2026, number guessing game

import random
print("Hey! Guess what number I'm thinking about. You have TEN guesses, and its from 1-100.")
# variable
number = random.randint(1,101)
count = 1

# range is 1-100
# Number of guesses is 10

#While loop
while count <= 10:
    guess = int(input("Your guess: "))
    if guess == number:
        print(f"Got it. It only took you {count} guesses.")
        break
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    count += 1

if count >= 10:
    print(f"Ten guesses and you still couldn't guess it?!? It was {number}...")