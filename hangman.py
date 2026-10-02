# AB, Hang man
import random

# list of 10 words on seperate text file

# another text file  holds win/loss counts (start with 0,0)

# read files

#use split(",") on content of the words txt doc to create list of words

# pull win and loose totals from other txt file and save them as 2 seperate variables

######   build hangman game

# save correct word as a varaible "random.choice(name of list)"

# varaible for  wrong guesses
incorrect = 0
# varable for guessed letters
guessed = ""

# function to display hangman (needs wrong guesses)
def display(incorrect):
    if incorrect == 0:
        print("""______
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
    return display      

        

##### function to show the letters and spaces (the correct word, letters that have been guessed)
def letter(word,guessed):
    # variable for display word (starts as an empty word)
    display_word = ""
    #loop over the correct word (look at every letter)
    for let in word:
        # check if letter had been guessed
        
            # then add the letter to display word

        # if they havent guessed letter

            #add underscore to display word

# return finished display word (OUTSIDE OF LOOP)


#### Main game loop (while true)
    # call function to show hangman
    # print function tcall to show display word
    # creat variable (ask user to guess letter)
    # add letter to list of guessed letters
    # check "if not letter in word:"
        # increase incorrect guesses
    # check of display word is same as word (call function)
        # tell user they won
        #increase win total
        #ask if they want to play again
            #reset random word, wrong guess ocunt and guessed letters
    #check if they lost (6 wrong guesses)
        #tell them they lost
        # say what word was
        #increase lose count
        # ask if they want to play again