import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
pen = turtle.Turtle()

count = 0
state_dict = {}
missing_states = []
data = pandas.read_csv("50_states.csv")
for state in data["state"]:
    state_dict[state] = 0
game_is_on = True

while game_is_on:
    if state_dict == {}:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{sum(state_dict.values())}/50 States Guessed", prompt="What's another state's name?").title()
    if answer_state in data["state"].tolist():
        if answer_state in state_dict:
            state_dict[answer_state] = 1
        new_state = data[data["state"] == answer_state]
        pen.hideturtle()
        pen.speed("fastest")
        pen.penup()
        pen.goto((int(new_state["x"]), int(new_state["y"])))
        pen.write(answer_state)
    if answer_state == "Exit":
        for state in state_dict:
            if state_dict[state] == 0:
                missing_states.append(state)
                missing_df = pandas.DataFrame(missing_states)
                missing_df.to_csv("missing_states.csv")
        # missing_states = [state for state in data["state"] if state not in list(state_dict.keys())]
        break
    if sum(state_dict.values()) == 50:
        game_is_on = False
        pen.goto(0,0)
        pen.write("Congratulations! You won!", align="center", font=("Courier", 40, "normal"))

turtle.mainloop()