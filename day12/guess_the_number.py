import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

## Functions to be used
# Function to set the difficulty
def set_difficulty():

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        return EASY_ATTEMPTS
    elif difficulty == 'hard':
        return HARD_ATTEMPTS

# Function to check the guess and number of attempts remaining
def check_answer(guess, number, attempts):
    '''Checks the guess against the actual number. Returns the number of attempts remaining.'''
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else: 
        print(f"You got it! The answer was {number}.")

## Game begins
def game():
    # Welcome message
    print(logo)
    print("Welcome to the Number Guessing Game!") 
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    # User chooses difficulty
    attempts = set_difficulty()

    # Guessing begins
    guess = 0
    while guess != number and attempts > 0:

        print(f"You have {attempts} attempt(s) remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)

    if attempts == 0:
        print(f"You've run out of guesses, you lose. The correct number was {number}.")
    else:
        print("Congratulations, you've won and guessed the correct number!")

game()