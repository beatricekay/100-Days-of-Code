from art import logo
from art import vs
from data import data_list
import random
import os 

# Define clear() function
def clear(): # putting it in a function so you can use it many times
  os.system('clear') # clears console

# Define draw_names() function
def draw_names():
    a = random.choice(data_list)
    b = random.choice(data_list)

    # If both a and b are the same, redraw b
    if a == b:
        b = random.choice(data_list)
    return a, b

def game():
    score = 0
    correct = True

    while correct == True:

        a,b = draw_names()

        print(logo)
        
        right_message = f"You're right! Current score: {score}."

        if score > 0:
            print(right_message)

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ") 

        if (a['follower_count'] > b['follower_count'] and answer == 'A') or (b['follower_count'] > a['follower_count'] and answer == 'B'):
            score += 1
            correct = True
            clear()
        else:
            clear()
            print(f"Sorry that's wrong. Final score: {score}")
            correct = False

game()