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


crypt = input("Am I (E)ncrypting or (D)ecrypting? :   ").upper().strip()
message = input("Message:  ").lower().strip()
shift = int(input("Shift amount:  "))

def cipher(message, shift):
    let = ""
    for character in message:
        if character.isalpha():
            character = ord(character)
            character = character + shift 
            if character >= 122:
                character = character - 26
            character = chr(character)
            let = let + character
        else:         
            character = ord(character)
            character = character + shift 
            if character >= 122:
                character = character - 26
            character = chr(character)
            let = let + character
            

            let = let + character
    return let
if message == "D":
    shift = 0 - shift



print(cipher(message, shift))


        
