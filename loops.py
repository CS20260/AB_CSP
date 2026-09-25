# AB, Notes Loops
import random
count = 1 #1st part of a loop is a START POINT

while count <= 10:# 2nd. STOP POINT (alwasy Boolean)
    print(count)
    count += 1 # 3rd increase iterator (counter of the number of times you've done somthing (iteration))


ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break # ends loop
    print("Duck....")
    ducks += 1

print(" GOOSE!!!!!!!!!!!")

#  continue => sends you cack to the begining (RESTARTS)





### Complex Data Type => hold other dats in it

siblings = ["Mathis", "Xander", "Hannah"] #   => surrounded by brackets   => items seperated by commas   => every item MUST be a valid data type
print(siblings)
print(siblings[0])
# adding to the list
siblings.append("Hallie") #<= append adds to the end of a list
print(siblings)
siblings.insert(1,"Alexia")
print(siblings)
 # REMOVE ITEM
siblings.pop(1) # if no index number it will remove LAST on list
print(siblings)
# print each item in a list
for sibling in siblings:
    print(sibling)


################################## FOR LOOP ##################################

# key word is "for"
# mini variable (only for that loop( current value (itteration)))
# key word "in"
# list (ALWAYS refrence a list)
# :
    # next line is indented

for num in range (1,25): # range bulids a list
    if num % 15 ==0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else: 
        print(num)
