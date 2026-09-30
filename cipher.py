# AB, Cipher Code, 30/9/2026

########### HELPFUL HINTS ############
    # ord convert character into ascii #        chr gives you ascii character
    # look at suggested output
    # start without function
    #3 variable user inputs
    # build working loop to print out every letter
    # condidtional in loop to see if letter is a letter then, convert to number, increace, convert back, print
    # variable to save letter as you change (or dont to keep  , .  ect..)
    # if pass end, maybe subtract to go back to beging of abc
    # TO DECRIPT same steps back. number user gives you becomes negitive


doing_what = input("Am I (E)ncrypting or (D)ecrypting? :   ").upper().strip()
message = input("Message:  ").lower().strip()
shift = int(input("Shift amount:  "))
let = ""
def cipher( doing_what, message, shift, let):
    for character in message:
        if character.isalpha():
            character = ord(character)
            character = character + shift 
            if character >= 122:
                character = character - 26
            character = chr(character)
            let += character
            
        
