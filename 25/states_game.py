import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

count = 0
state_dict = {}
data = pandas.read_csv("50_states.csv")
game_is_on = True

while game_is_on:
    if state_dict == {}:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{sum(state_dict.values())}/50 States Guessed", prompt="What's another state's name?").title()
    if answer_state in data["state"].tolist():
        if answer_state not in state_dict:
            state_dict[answer_state] = 1
        new_state = data[data["state"] == answer_state]
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed("fastest")
        pen.penup()
        pen.goto((int(new_state["x"]), int(new_state["y"])))
        pen.write(answer_state)
    if sum(state_dict.values()) == 50:
        game_is_on = False
        pen.goto(0,0)
        pen.write("Congratulations! You won!", align="center", font=("Courier", 40, "normal"))

turtle.mainloop()