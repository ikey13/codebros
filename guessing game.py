import random
def guess_number():
    secret_number + random.randint (1, 25)
    attempts = 0
    print("welcome to my number guessing game")
    print("i have a number in between 1 and 25")
    
    while true: 
        guess = int(input("enter your guess"))
        attempts += 1
        if guess < secret_number:
            print("too low. try again")
            if guess > secret_number:
                print("too high. try again")
                print(f"congratulations! you guessed the number {secret_number} correctly in {attempts} attempts")