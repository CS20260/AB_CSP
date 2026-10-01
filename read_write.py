# AB, reading and writing to files
# saves code in between runs

# \/ lets you open file
#        \/ action (means this is a function)
#           \/ file path   \/  what we do with this file (w)rite or (r)ead (r+)read and appending
#                                \/ naming file in code
with open("practice.txt", "r+") as file:
#       \/ name so that we can use this
#                    \/ gives what is written on the file
    content = file.read()
#               ^ name of file
    content = "Chapter 1:\n" + content+ "And Christopher Robin was sitting on his door step putting on his big boots."
    file.write(content)



###### when we write on a flie it replaces the contents ######
#with open("practice.txt", "w") as file:
#    file.write("Winnie the Pooh and the Blustery Day")


#                          \/ append (adds contend to the end)
with open("practice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day")



