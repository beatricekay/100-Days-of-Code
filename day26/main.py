import pandas as pd

# Read NATO alphabet file
path = '/Users/beatricekaystacs/Downloads/NATO-alphabet-start/nato_phonetic_alphabet.csv'
df_nato = pd.read_csv(path)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in df_nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:")
code_word = [nato_dict[letter.upper()] for letter in word]
print(code_word)