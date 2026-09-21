# AB, 18/9/2026, Strings

# stings are a data type => any data saved inside of quotation marks "" ''  user input ==sting
# data types = how you store information

name = "Will"

age = input("How old are you: ")
print(type(age))

print(age*14 ) # => repetes string that # of times   


####   ===> Concatenation => puts 2 strings directly next to each other use + sign
print(name + " " + "Hickman")

# SINTAX == string.action/method()

name = input("What is your name: ").strip().capitalize()

#
sentence = "The quick brown fox jumped over the lazy dog." 
print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name)) # gets length of string

print(f"Your name is {name}. That is {len(name)} letters long. Your first inital is {name[0]} I think I will call you {name[0:4]}")
# f string => formated string. use curly brackets to break quoteations (write code inside)
# slice => take a big string and pull out a smaller piece
