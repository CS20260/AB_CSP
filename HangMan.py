# Hangman.py Alexia Boone

#day 1 __ variables created, function dysplay  x
# day 2__ scaffold function (conditional), while True loop, add letters  x
# Day #3 __ increase wrong guesses, check to see if won, check to see if lost
# word list (10)
import random
# (possible words
# guess list
#body parts (list)
# word for round)
wordlist = ("duck", "hat", "rythm", "truck", "plane", "friend", "word", "trap", "class", "dead", "womp", "gag", "tan", "rat", "blood", "enter", "four", "flour", "six", "seven", "loser", "loose", "zebera", "happy", "sad",)
guesslist = []
bodyparts = 0
word = random.choice(wordlist)


#function for word display (takes in guessed letters(whole list) , word for round)
def display(guesslist, word):
    # variable that has current display (words)
    display = ""
    # look at each letter in guesslist
    for letter in word:
        # check to see if letter is in the word
         if letter in guesslist:
            # add the letter to current display
            display += letter
        # otherwise
         else:
             #Add an _ to the current display
            display += "_"
    # return the current display
    return display
         



   
#function to print scaffold at correct wrong level (takes in wrong guesses)
def scaffold():
    #conditional to check level and print correct image 
    # # if wrong = 0
        # print(""" ___
         #          |  |
         #          |
         #          |
         #          |_____
        # """)
    if bodyparts == 0:
        print(""" ___
                 |    |
                 |
                 |
                 |
                 |
                 |_______ """)
    elif bodyparts == 1:
     print(""" ___
             |    |
             |   (_)
             |
             |
             |
             |_______ """)
    elif bodyparts == 2:
     print(""" ___
             |    |
             |   (_)
             |    |
             |
             |
             |_______ """)
    elif bodyparts == 3:
     print(""" ___
             |    |
             |   (_)
             |    |\\
             |
             |
             |_______ """)
    elif bodyparts == 4:
        print(""" ___
                 |    |
                 |   (_)
                 |   /|\\
                 |
                 |
                 |_______ """)
    elif bodyparts == 5:
        print(""" ___
                 |    |
                 |   (_)
                 |   /|\\
                 |   /
                 |
                 |_______ """)
    elif bodyparts == 6:
        print(""" ___
                 |    |
                 |   (xx)
                 |    /|\\
                 |    / \\
                 |
                 |_______ 
                   YOU'RE DEAD! """)
    return scaffold

# randomly select word from list of possible words
# while True (put in function to randomly select word)
while True:
        
        #call function to print scaffold
        scaffold()
        # print function to display word
        print(display(guesslist, word))
        # print guessed letter variable
        print(guesslist)
        # create letter variable equal to user input asking for a letter (strip and lowercase)
        u = input("Give me a letter.").strip().lower() #Strip and lowercase
        # add letter to guessed letters
        guesslist.append(u)
        # if letter is not in word
        if u not in word:
 # increase wrong guesses
            bodyparts += 1




# check to see if they have won or lost #check if word matches word display function
        if display(guesslist, word) == word:
            print("You won!")# tell the user they won
            replay = input("""
                           Do you want to replay?""")
            if replay == "no":
                break
            else:
                print()
        elif bodyparts >= 6: # check if there are 6 wrong guesses
            scaffold()# call scaffold function
            print("You lost, womp womp")
            print("correct word was " + word + "...")#show correct word
            replay = input("""
                           Do you want to replay?""")
            if replay == "no":
                break
            else:
                print()
            
        #(tell user they lost) *don't need included it w/ display

# repeat code)