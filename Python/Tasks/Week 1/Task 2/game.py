# Create a number guessing game where the program randomly selects a number between 1-100, and the user has to guess it.

import random

while True:
    guessNumber = int(input("Enter the random number between 1-101 "));

    randomNumber = random.randrange(1,101)

    if guessNumber==randomNumber:
        print("You guess the right number")
        break;
    else:
        print("You guess the wrong number, the random number is ",randomNumber)