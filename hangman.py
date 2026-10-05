# AB, Hang man
import random

# list of 10 words on seperate text file

# another text file  holds win/loss counts (start with 0,0)

# read files
with open("words.txt","r") as file:
    words= file.read().split(",")
with open("win_loss.txt", "r")as file:
    win_loss = file.read()
#use split(",") on content of the words txt doc to create list of words

# pull win and loose totals from other txt file and save them as 2 seperate variables

######   build hangman game

# save correct word as a varaible "random.choice(name of list)"
word = random.choice(words)
# varaible for  wrong guesses
incorrect = 0
# varable for guessed letters
guessed = []

# function to display hangman (needs wrong guesses)
def scaffold (incorrect):
    if incorrect == 0:
        print(""" ______
                 |      |
                 |       
                 |
                 |
                 |_________  """)
        
    elif incorrect == 1:
        print("""______
                |      |
                |     (oo) 
                |     
                |  
                |_________  """)
        
    elif incorrect == 2:
        print("""______
                |      |
                |     (oo) 
                |      ||
                |  
                |_________  """)

    elif incorrect == 3:
        print("""______
                |      |
                |     (oo) 
                |     /||
                |     
                |_________  """)
        
    elif incorrect == 4:
        print("""______
                |      |
                |     (oo) 
                |     /||\\
                |     
                |_________  """)
        
    elif incorrect == 5:
        print("""______
                |      |
                |     (oo) 
                |     /||\\
                |     /
                |_________  """)
        
    else:
        print("""______
                |      |
                |     (xx)
                |     /||\\ 
                |     /  \\ 
                |__________  """)
    return scaffold


        

##### function to show the letters and spaces (the correct word, letters that have been guessed)
def display(word,guessed):
    # variable for display word (starts as an empty word)
    display_word = ""
    #loop over the correct word (look at every letter)
    for let in word:
        # check if letter had been guessed
        if let in guessed:
            # then add the letter to display word
            guessed += let
        # if they havent guessed letter
        else:
            #add underscore to display word
            display_word += "_"
    return display
    # return finished display word (OUTSIDE OF LOOP)


#### Main game loop (while true) 
while True:
    # call function to show hangman
    print(scaffold(incorrect))
    # print function (call) to show display word
    print(display(word,guessed))
    # creat variable (ask user to guess letter)
    user = input("Guess a letter: ").strip().lower()
    # add letter to list of guessed letters
    guessed.append(user)
    # check "if not letter in word:"
    if user not in word:
        # increase incorrect guesses
        incorrect += 1
    # check of display word is same as word (call function)
    if display == word:
        # tell user they won
        print("You got it!")
        #increase win total
        win += 1
        #ask if they want to play again
        replay = print("Do you want to play again? Yes or No.").strip().lower()
        if replay == "no":
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
        replay = print("Do you want to play again? Yes or No.").strip().lower()
        if replay == "no":
            break
        elif replay == "yes":
            # reset variables
            word = random.choice(words)
            # (varaible for  wrong guesses)
            incorrect = 0
            # (varable for guessed letters)
            guessed = []