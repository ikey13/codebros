weight = int(input("Weight: "))
unit= input("(L)bs or (K)g: ")
if unit == "l" or "L":
    print("You weight: ")
    print(str((weight / 2.2)) + " kg's")
elif unit == "k" or "K":
    print("You weight: ")
    print(str((weight * 2.2)) + " lb's")