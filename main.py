import turtle
import pandas



screen=turtle.Screen()
screen.title("Name of the states")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
gussed_state=[]
while len(gussed_state) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_state)}/50", prompt="What is the name of State?").title()
    if answer_state=="Exit":

        missing_state=[]
        for state in all_states:
            if state not in gussed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state")

        break

    if answer_state in all_states:
        gussed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


#need to print the states which we have not guessed