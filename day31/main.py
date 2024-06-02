from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {} # ensure next_card() and flip_card() are referencing the same word

## READ DATA
# read the data from the csv file
try:
    data = pd.read_csv("/Users/beatricekay/Downloads/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("/Users/beatricekay/Downloads/flash-card-project-start/data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    # convert df to dictionary where the key in each dictionary is the column name
    to_learn = data.to_dict(orient = "records")

##########################################################################################

## FUNCTIONS
# function to change the word
def next_card():
    global current_card # ensure word is saved to the global current_card dictionary
    global flip_timer # ensure the timer is reset for every new French word
    window.after_cancel(flip_timer) # cancel the timer for the previous French word
    
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img) # change back to white card
    
    # saved to global flip timer
    flip_timer = window.after(3000, func=flip_card) # flip card for every new French word
    
# function to flip the card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img) # change to green card
    
# function to keep track of learned and unlearned words
def is_known():
    to_learn.remove(current_card) # if word is known, remove it from list of words to learn
    data = pd.DataFrame(to_learn)
    data.to_csv("/Users/beatricekay/Downloads/flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()

##########################################################################################

## UI CODE
# create flashcard window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) # set background of flashcard

# change to the English word after 3 seconds ONLY for the first card
flip_timer = window.after(3000, func=flip_card) # milliseconds

# add flashcard image
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="/Users/beatricekay/Downloads/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="/Users/beatricekay/Downloads/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# add language, e.g. French
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))

# add actual French word
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# add buttons
cross_image = PhotoImage(file="/Users/beatricekay/Downloads/flash-card-project-start/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="/Users/beatricekay/Downloads/flash-card-project-start/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# call the function so that the first card shows the correct text
next_card()

window.mainloop()