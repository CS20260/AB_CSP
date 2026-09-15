#AB, fixing user inputs

while True: # While true loop => repeat till break
    color = input("Tell me a color that is only one word:  ").strip().lower() # <= gets rid of extra spaces <= gets rid of all capital letters can do capatilize, upper, title,
    if color.isnumeric():# <= if checks to see if true. if not true move on
        print("That is a number not a color...")
    elif " " in color: #<= check to see if true. if false, move on
        print(" I said ONE word...")
    else: # <= happens of everything else is false
        break # <= end loop
print(f"We painted the walls {color}!")