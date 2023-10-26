import turtle, pandas
IMAGE = "blank_states_img.gif"
WIDTH=745
HEIGHT=491
FONT=("Arial", 8, "normal")

#Initialize the screen with the map
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

#Listen for mouse clicks:
#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

def print_usstate(state_name, position):
    t = turtle.Turtle()
    t.hideturtle()
    t.pu()
    t.goto(position)
    t.write(state_name, align="center", font=FONT)
    #t.goto((0,0))


#Read csv with States data
data = pandas.read_csv("50_states.csv")
us_states = data.state.to_list()
states_guessed = []
end_game = False

while len(states_guessed) <= 50 and end_game == False:
    answer_state = screen.textinput(title=f"States correct {len(states_guessed)}/50",
                                    prompt="""What's another state's name? ('exit' to
                                    finish, csv file with missing states
                                    generated)""").title()
    if answer_state in us_states and answer_state not in states_guessed:
        print_usstate(answer_state.title(),
                      (int(data[data.state == answer_state.title()].x),
                       int(data[data.state == answer_state.title()].y)))
        states_guessed.append(answer_state)
    elif answer_state.lower() == "exit":
        #Get states not guessed:
        study_states = [state for state in us_states if state not in
                        states_guessed]
        #Create a Series from it
        states_series_csv = pandas.DataFrame(study_states).rename_axis(
                "States to study").to_csv("states_to_learn.csv")

        end_game = True

