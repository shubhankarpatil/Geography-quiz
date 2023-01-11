from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()

screen.title("USA Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="Guess another state name").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_state.append(answer)
        turtle.penup()
        turtle.hideturtle()
        to_get = states[states.state == answer]
        turtle.goto(int(to_get.x), int(to_get.y))
        turtle.write(answer)

print(missing_states)
# not_answered = list(set(all_states) - set(guessed_state))