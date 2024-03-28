name = input("What's your name? ")
length_of_name = int(len(name))
if length_of_name < 3:
    print("Sorry, the name inputed must be 3 or more characters.")
elif length_of_name > 50:
    print("The name inputed must be below 50 characters")
else:
    print("Hey" + name + ",looks good!")