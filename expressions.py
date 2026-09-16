# intergers, floats, and expressions notes

# integers => whole number
students = 23
cars = 50
computers = 29
awareness = -12

# Float => numbers with decimals
pi = 3.14159
temp = -95.6
cost = 1.99
rain = 2.17

# Arithmetic Operatiors (* multiplication  -subtraction  / division  + addition  ** exponents  % modulo/moduloud/mod  //intiger division)
print(f"The remainder of 18%4 is {18%4}")
print(f"The remainder of 18%5 is {18%5}")

print(f"18/4 is {18/4} or {18//4} with a remainder of {18%4}")
print(f"18/4 is {18/5} or {18//5} with a remainder of {18%5}")

# order of operations
average = (85+66+94+72)/4
print(f"the avarage is {average}")

grades = [85,66,94,72,88,79,100]
students = len(grades)
average = sum(grades)/students
#                        v inputs are always strings
print(f"the avarage is {int(average)}") # int => integer  float=> float  str=> string
#                               ^ what to convert

# convert data type
price = float(input("How much did the item cost: "))
tax = 0.0485
sales_tax = price * tax 
total = price + sales_tax
print(f"Your total is {total}")