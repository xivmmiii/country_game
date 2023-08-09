import turtle
import pandas
screen=turtle.Screen()
screen.title("India States Game")
image="india_main.gif"
screen.addshape(image)
turtle.shape(image)

turtle.setup(500,500)
data=pandas.read_csv("states.csv")
all_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<len(data.state):
    answer_state=screen.textinput(title=f"{len(guessed_states)} states guessed",prompt="What's another state's name?")
    print(answer_state)
    if answer_state=='exit':
        missing_states = [states for states in all_states if states not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        state_data=data[data.state==answer_state]
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())  #or answer_state can be used directly
    ##to get coordinates
    # def get_coor(x,y):
    #     print(x,y)
    # turtle.onscreenclick(get_coor)

turtle.mainloop()