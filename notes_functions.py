# AB, Function notes
# use functions on repetitive code
# makes code esiar to read
# smaller chunks

def stupid_proof(money):
    while True:
        try:
         amount = float(input(f" what is your monthly {money}:"))
         return amount
        except:
           print("That is not a number :( ")

#variables
income = stupid_proof("income")


rent = stupid_proof("rent")


utilities = stupid_proof("utilities")


groceries = stupid_proof("groceries")


transportation = stupid_proof("transporation")


savings = income * .1

# functions
#\/ def = define
#       \/ name function (rules are same as variables) holds actions
#               \/ paren then parameters (peices of info needed for program to run)
def calc_percent(income, bill):

#       \/ return is an out put to function call
#                   \/ use parameters as values
    return round(bill/income * 100)



# outputs for user                        \/ function call  \/arguments (value of variable when you run function)
print(f"Your rent is ${rent:.2f} that is {calc_percent(income, rent)}% of your savings. Your utilities is ${utilities:.2f} that is {calc_percent(income,utilities)}% of your savings. Your groceries is ${groceries:.2f} that is {calc_percent(income,groceries)}% of your savings. Your transportations is ${transportation:.2f} that is {calc_percent(income,transportation)}% of your savings. You should save ${savings:.2f} that is {calc_percent(income, savings)}% of your income.")


print(f"You have $ {income-rent-utilities-groceries-transportation-savings} left")






