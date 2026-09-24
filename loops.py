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

print(siblings[0])