import turtle
import os
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Load U.S. map
image = "/Users/beatricekay/Downloads/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Save 50 states in a list
country_csv_path = "/Users/beatricekay/Downloads/day-25-us-states-game-start/50_states.csv"
df_state = pd.read_csv(country_csv_path, encoding='utf-8')
all_states = df_state["state"].tolist()
guessed_states = []
no_of_guessed_states = len(guessed_states)

while no_of_guessed_states < 50:
    # Keep asking question if haven't guessed all states
    answer_state = screen.textinput(title=f"{no_of_guessed_states}/50", 
                                    prompt="What's another state's name?").title()
    print(answer_state)
    
    # Create a list of all the unguessed states once the game has ended
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append[state]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    # If answer is one of the 50 states
    if answer_state in all_states:
        
        # Save state in guessed_states list if correct
        guessed_states.append(answer_state)
        
        # Create a turtle to write the name of the state at the state's x and y coordinate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df_state[df_state["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)

screen.exitonclick()