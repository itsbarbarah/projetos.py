import random
number = random.randrange (0,50)
guess = int (input("Guess a number between 0 and 50: "))

while guess != number:
    if guess < number:
        print("You need to guess higher. Please, try again.")
        guess = int(input("\nGuess a number between 0 and 50: "))
    else:
        print("You need to guess lower. Please, try again.")
        guess = int(input("\nGuess a number between 0 ad 50: "))
print("You guessed the number correctly!")
