# AB, Silly Sentences, 9/21/2026

# veriables
person = input("Tell me a person : ").strip().capitalize()
smell = input("Tell me a smell : ").strip().lower()
verb = input("Tell me a verb that ends in 'ing' : ").strip().lower()
adjective = input("Tell me a adjective **not ending in 'ing' ** : ").strip().lower()
item = input("Tell me an item : ").strip().lower()
word = input("Tell me a word or phrase : ").strip().upper()

#print the sentence
print("My prom date was actually " +  person + ", who showed up in a limousine that smelled like " + smell + ". The second we stepped onto the dance floor, "+ person +" completely ignored the music and started "+ verb +" in the corner by the drinks. When the principal told "+ person +" to relax, "+ person +" ran from the room, claiming to be "+ adjective +". During the hasty retreat from the room "+ person +" smashed the punch bowl with a rusty "+ item +" while loudly screaming, "+ word +"!")