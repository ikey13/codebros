started = False
command = ""
while True:
    command = input("> ").lower()
    if(command) == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car has started ready to go!")
    elif(command) == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif(command) == "help":
        print("""
Start - Start the car.
Stop - Stop the car
Quit - End game.
        """)
    elif(command) == "quit":
        break
    else:
        print("Sorry, I don't understand that...")