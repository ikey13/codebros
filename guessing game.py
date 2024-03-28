import random
secret_number = random.randint(1,10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    elif guess > secret_number:
        print("Your guess is too big")
    elif guess < secret_number:
        print("Your guess was too small")
else:
    print("You lose!")
    print(f"The secret number was {secret_number}!")