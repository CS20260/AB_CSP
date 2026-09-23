# AB, 23/9/2026, Password Strength Checker

# variables
length = False
upper = False
lower = False
number = False
symbol = False
strength = 0
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
        uppper = True

    # check if lower
    if letter.islower():
    # update variable
        lower = True

    # check if numeric
    if letter.isnumeric():
    # update variable
        number = True

    # if letter in " list possibilities ((!@#$%^&*()<>,.?/))":
    if letter in "!@#$%^&*()_+-=`~[]\{}|;':<>?,./":
    # update variable
        symbol = True

# veriable to check strength
if length is True:
    strength += 1

if upper is True:
    strength += 1

if lower is True:
    strength += 1

if number is True:
    strength + 1

if symbol is True:
    strength + 1

if password is 0:
    password_strength = " VERY WEAK.."

if password is 1:
    password_strength = "weak.."

if password is 2:
    password_strength = "kinda weak"

if password is 3:
    password_strength = "low medium.."

if password is 4:
    password_strength = "medium"

if password is 5:
    password_strength = "strong!"

# tell user how to fix
if length is False:
    
# # tell user if true or false for each thing

print(f"""Your password has:
    At least 8 characters: {length}
    An uppercase letter: {upper}
    A lowercase letter: {lower}
    A number: {number}
    A symbol: {symbol}
Your password strength is {password_strength}
""")

