# Task: Create a letter using starting_letter.txt for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend" under the format "letter_for_{name}.txt"

# Hint 1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint 2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint 3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Helpful Link: https://www.pythontutorial.net/python-basics/python-read-text-file/

import os
os.getcwd()

## Step 1: Read names from invited_names.txt file
names_path = './Input/Names/invited_names.txt'
with open(names_path, mode="r") as file_names:
    # .readlines() helps to put each line in a list
    name_list = file_names.readlines()
    print(name_list)

## Step 2: Remove the \n from each name
name_list_updated = []
for name in name_list:
    name_cleaned = name.replace("\n", "")
    name_list_updated.append(name_cleaned)
    
print(name_list_updated)

## Step 3: Read the starting_letter.txt
letter_path = './Input/Letters/starting_letter.txt'

with open(letter_path, mode="r") as file_letter:
    # .read() puts the entire text into a string
    letter = file_letter.read()
    print(letter)

## Step 4: Replace [name] in letter with name from name_list_updated
for name in name_list_updated:
    letter_updated = letter.replace("[name]", name)
    final_letter_path = './Output/ReadyToSend/' + f'letter_for_{name}.txt'
    with open(final_letter_path, mode="w") as final_letter:
        final_letter.write(letter_updated)