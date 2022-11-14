#Step 4

import random



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letters in range(word_length):
    display += "_"

# Guessing process
while "_" in display or end_of_game == False:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter starting from first to last letter against the guess
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(display)
            
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    final_word = f"{''.join(display)}"
    print(final_word)

    if guess not in chosen_word:
      lives -= 1
    
    if lives < 1:
      end_of_game = True
      print("You lose.")

    #Check if user has got all letters.
    if final_word == chosen_word:
      end_of_game = True
      print("You win.")

    print(lives)
  

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
print(stages[lives])