rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# 0 = Rock, 1 = Paper, 2 = Scissors
import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user != 0 and user != 1 and user != 2:
    print("You typed an invalid number, you lose!")

else:

    options = [rock, paper, scissors]
    computer = random.randint(0, 2)
    result = str(user) + str(computer)
    user_win = ["10", "02", "21"]
    draw = ["00", "11", "22"]

    print(options[user])
    print(f"Computer chose {computer}")
    print(options[computer])

    if result in user_win:
        print("You win")
    elif result in draw:
        print("It's a tie")
    else:
        print("You lose")

