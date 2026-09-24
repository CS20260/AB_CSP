# AB, 23/9/2026, Password Strength Checker

# variables
length = False
upper = False
lower = False
number = False
symbol = False
strength = 0
password_strength = ""
    # ask user for password
password = input("Enter your password here: ")

# for loop to check letters 
for letter in password:

    # check to see if password is long enough
    if len(password) >= 8:
    # update variable
        length = True

    # check if upper 
    if letter.isupper():
    # update variable
        upper = True

    # check if lower
    if letter.islower():
    # update variable
        lower = True

    # check if numeric
    if letter.isnumeric():
    # update variable
        number = True

    # if letter in " list possibilities ((!@#$%^&*()<>,.?/))":
    if letter in "!@#$%^&*()_+-=`~[]{|};':<>?,./":
    # update variable
        symbol = True

# variable to check strength
if length == True:
    strength += 1

if upper == True:
    strength += 1

if lower == True:
    strength += 1

if number == True:
    strength += 1

if symbol == True:
    strength += 1



if strength == 0:
    password_strength = " VERY WEAK.."

if strength == 1:
    password_strength = "weak.."

if strength == 2:
    password_strength = "kinda weak"

if strength == 3:
    password_strength = "low medium.."

if strength == 4:
    password_strength = "medium"

if strength == 5:
    password_strength = "strong!"

# tell user how to fix
    
# # tell user if true or false for each thing

print(f"""Your password has:
    At least 8 characters: {length}
    An uppercase letter: {upper}
    A lowercase letter: {lower}
    A number: {number}
    A symbol: {symbol}
Your password strength is {password_strength}
    If you don't have a strong password, make sure you have:
        8 characters
        an uppercase letter
        a lowercase letter
        a number
        a symbol
    
    If you are missing any of these, FIX IT!!!!!!""")

