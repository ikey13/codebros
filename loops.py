length = int(input("Length: "))
width = int(input("Width: "))

def main():
    print_rectangle(length,width)

def print_rectangle(length,width):
    for i in range(length):
        for i in range(width):
            print("#", end = " ")
        print()
main()