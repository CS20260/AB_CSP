# AB, 22/9/2026, CONDITIONALS NOTES
#$##### conditional <= helps make desions based on a boolean (boolean <= data type that is true or false)

# conditional

time = 1416
day = "Tuesday"

# conditinals always begin with if
if time < 1200 and time > 500            # then a boolean statement  # end line with Colen
    print("Good Morning.... I guess.")              #next line must be indented because of colen
elif time < 1700:
    print("Good Afternoon.")
    if day != "Saturday" and day != "Sunday":
        print("How was school today?")
elif time < 2000:
    print(" Good Evening.")
else                                     # won't happen unless condition above is True ## frequently marks the end  ### if every thing else is false do this
    print("Good Night.")


print("Code is done")

###### comarison operator    <  >  == <=  >=  != not equal
###### logical operators     and <= both conditions must be true     or <= at least one MUST be true       not<= check to see if false