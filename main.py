import turtle

import pandas

FONT = ("Courier", 8, "normal")
screen = turtle.Screen()
screen.title("us_states_game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)
game_not_done = True
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
num_of_correct_answer = 0
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(0, 280)
all_states = data.state.values
done_list = []
while game_not_done:
    score.clear()
    score.write(f"{num_of_correct_answer}/50", align="center", font=("Courier", 20, "normal"))
    answer_state = screen.textinput(title=f"GUESS STATE", prompt="What's Another State Name?").capitalize()
    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in done_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_you_missed.csv")

        break
    elif answer_state not in done_list:
        if answer_state in all_states:
            state = data[data.state == answer_state]
            x = int(state.x.values)
            y = int(state.y.values)
            writer.goto(x, y)
            writer.write(f"{answer_state}", font=FONT)
            num_of_correct_answer += 1
            done_list.append(answer_state)
    if num_of_correct_answer == 50:
        game_not_done = False


screen.mainloop()
