import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_df = pd.read_csv("50_states.csv")
all_states = states_df.state.tolist()
all_states_num = len(all_states)
states_guessed = []

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.penup()

while len(states_guessed) < all_states_num:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/{all_states_num} States Correct",
                                    prompt="What another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        state_data = states_df[states_df["state"] == answer_state]
        my_turtle.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        my_turtle.write(answer_state)
        states_guessed.append(answer_state)

states_to_learn = states_df[~states_df.isin(states_guessed)]
states_to_learn = states_to_learn.dropna()
states_to_learn = states_to_learn.state
states_to_learn.to_csv("states_to_learn.csv")
print(states_to_learn)