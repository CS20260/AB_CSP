# AB, Hang man
import random

# list of 10 words on seperate text file

# another text file  holds win/loss counts (start with 0,0)

# read files
with open("words.txt","r") as file:
    words= file.read().split(",")
with open("win_loss.txt", "r")as file:
    win_loss = file.read().strip().split(",")
#use split(",") on content of the words txt doc to create list of words
#turn win loss into an integer so that we can concatinate
# pull win and loose totals from other txt file and save them as 2 seperate variables
win = int(win_loss[0])
loss = int(win_loss[1])
######   build hangman game

# save correct word as a varaible "random.choice(name of list)"
word = random.choice(words)
# varaible for  wrong guesses
incorrect = 0
# varable for guessed letters
guessed = []

print(f"Wins: {win}, Losses : {loss}.")
##### function to show the letters and spaces (the correct word, letters that have been guessed)
def display(word,guessed):
    # variable for display word (starts as an empty word)
    display_output = ""
    #loop over the correct word (look at every letter)
    for letter in word:
        # check if letter had been guessed
        if letter in guessed:
            # then add the letter to display word
            display_output += letter
            
        # if they havent guessed letter
        else:
            #add underscore to display word
            display_output += "-"


    return display_output
    # return finished display word (OUTSIDE OF LOOP)




# function to display hangman (needs wrong guesses)
def scaffold (incorrect):
    if incorrect == 0:
        print("""
                 |      |
                 |       
                 |
                 |
                 |_________  """)
        
    elif incorrect == 1:
        print("""
                |      |
                |     (oo) 
                |     
                |  
                |_________  """)
        
    elif incorrect == 2:
        print("""
                |      |
                |     (oo) 
                |      ||
                |  
                |_________ """)

    elif incorrect == 3:
        print("""
                |      |
                |     (oo) 
                |     /||
                |     
                |_________ """)
        
    elif incorrect == 4:
        print("""
                |      |
                |     (oo) 
                |     /||\\
                |     
                |_________  """)
        
    elif incorrect == 5:
        print("""
                |      |
                |     (oo) 
                |     /||\\
                |     /
                |_________  """)
        
    else:
        print("""
                |      |
                |     (xx)
                |     /||\\ 
                |     /  \\ 
                |__________  """)
    return scaffold




#### Main game loop (while true) 
while True:
    # call function to show hangman
    scaffold(incorrect)
    #make the display print thing work (make it simplier)
    current_display = (display(word,guessed))
    # print function to show display word
    print(current_display)

    # creat variable (ask user to guess letter)
    user = input("Guess a letter: ").strip().lower()
    # make a space to make it look better 
    print("""


""")
    # add letter to list of guessed letters
    if user in guessed:
        print("""You guessed this already...
        
        
        """)
        continue
    guessed.append(user)
    # check "if not letter in word:"
    if user not in word:
        # increase incorrect guesses
        incorrect += 1

    # recheck if display word is same as word (call function)
    current_display = (display(word,guessed))
    # print function to show display word
    print(current_display)
    if current_display == word:
        # tell user they won
        print("You got it!")
        #increase win total
        win += 1
        #ask if they want to play again
        replay = input("Do you want to play again? Yes or No.").strip().lower()
        if replay == "no":
            with open("win_loss.txt", "w") as file:
                file.write(f"{win},{loss}")
                print(f"Wins: {win}, Losses : {loss}.")
            break
        elif replay == "yes":
            # reset variables
            word = random.choice(words)
            # (varaible for  wrong guesses)
            incorrect = 0
            # (varable for guessed letters)
            guessed = []
    #check if they lost (6 wrong guesses)
    if incorrect == 6:
        #tell them they lost
        print("You lost. You are a loser.")
        # say what word was
        print(f"The word was {word}.")
        #increase lose count
        loss += 1
        # ask if they want to play again
        replay = input("Do you want to play again? Yes or No.").strip().lower()
        if replay == "no":
            with open("win_loss.txt", "w") as file:
                file.write(f"{win},{loss}")
                print(f"Wins: {win}, Losses : {loss}.")
            break
        elif replay == "yes":
            # reset variables
            word = random.choice(words)
            # (varaible for  wrong guesses)
            incorrect = 0
            # (varable for guessed letters)
            guessed = []
