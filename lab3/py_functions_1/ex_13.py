"""
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.

This is how it should work when run in a terminal:


Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

from random import randint

def work():
    name = str(input("Hello! What is your name?\n"))
    
    num, counter = randint(1, 20), 0
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')

    guess = 0
    while num != guess:
        guess = int(input("Take a guess\n"))
        print('\n')

        if num > guess:
            print("Your guess is too low.")
        elif num < guess:
            print("Your guess is too big.")

        counter += 1
    
    print(f'Good job, KBTU! You guessed my number in {counter} guesses!')

work()