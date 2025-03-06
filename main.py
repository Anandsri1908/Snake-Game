import turtle
import time 
import random

delay=0.1

#Score
score= 0
high_score= 0

#set up the screen

hs= turtle.Screen()
hs.title("Snake Game")
hs.bgcolor("blue")
hs.setup(width=700, height=600)
hs.tracer(0) # turns off the screen updates

#snake head  
shead= turtle.Turtle()
shead.speed(0)
shead.shape("circle")
shead.color("red")
shead.penup()
shead.goto(0,0)
shead.direction="stop"


#Snake food
sfood= turtle.Turtle()
sfood.speed(0)
sfood.shape("square")
sfood.color("yellow")
sfood.penup()
sfood.goto(0,100)

portions= []

#mark
mark=turtle.Turtle()
mark.speed(0)
mark.shape("square")
mark.color("white")
mark.penup()
mark.hideturtle()
mark.goto(0, 260)
mark.write("Score: 0  High Score: 0",align="center", font=("Courier", 24, "normal"))

# Game Over display
gameover_mark = turtle.Turtle()
gameover_mark.speed(0)
gameover_mark.shape("square")
gameover_mark.color("white")
gameover_mark.penup()
gameover_mark.hideturtle()
gameover_mark.goto(0, 0)

# Start Game message
start_mark = turtle.Turtle()
start_mark.speed(0)
start_mark.shape("square")
start_mark.color("white")
start_mark.penup()
start_mark.hideturtle()
start_mark.goto(0, 0)
start_mark.write("Press 'i', 'k', 'j', 'l' to Start", align="center", font=("Courier", 24, "normal"))


#functions
def go_up():
    if shead.direction !="down":
        shead.direction="up"
    start_mark.clear()  # Clear the start message

def go_down():
    if shead.direction !="up":
        shead.direction="down"
    start_mark.clear()  # Clear the start message

def go_left():
    if shead.direction !="right":
        shead.direction="left"
    start_mark.clear()  # Clear the start message

def go_right():
    if shead.direction !="left":
        shead.direction="right"
    start_mark.clear()  # Clear the start message

def move():
    if shead.direction == "up":
        y = shead.ycor()
        shead.sety(y + 20)

    if shead.direction == "down":
        y = shead.ycor()
        shead.sety(y - 20)

    if shead.direction == "left":
        x = shead.xcor()
        shead.setx(x - 20)

    if shead.direction == "right":
        x = shead.xcor()
        shead.setx(x + 20)

#keyboard commands
hs.listen()
hs.onkeypress(go_up,"i")
hs.onkeypress(go_down,"k")
hs.onkeypress(go_left,"j")
hs.onkeypress(go_right,"l")

#Reset game function
def reset_game():
    global score, delay
    time.sleep(1)
    shead.goto(0, 0)
    shead.direction = "stop"

    #Hide the portions
    for portion in portions:
        portion.goto(1000, 1000)

    #clear the portions list
    portions.clear()

    #reset the score and delay
    score = 0
    delay = 0.1

    #update the score display
    mark.clear()
    mark.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


#Main Game loop 
while True:
    hs.update()

    #check for a collision  with the  border
    if shead.xcor() > 340 or shead.xcor() < -340 or shead.ycor() > 290 or shead.ycor() < -290:
        gameover_mark.write("Game Over!", align="center", font=("Courier", 36, "normal"))
        hs.update()  # Update the screen to show the message
        time.sleep(2)  # Keep the message on screen for 2 seconds
        gameover_mark.clear()  # Clear the message
        reset_game()  # Reset the game


    #check for a collision with the food
    if shead.distance(sfood)<20:  #move the food to random spot
        x=random.randint(-340,340)
        y=random.randint(-290,290)
        sfood.goto(x,y)

        #add a portion
        new_portion=turtle.Turtle()
        new_portion.speed(0)
        new_portion.shape("circle")
        new_portion.color("black")
        new_portion.penup()
        portions.append(new_portion)

        #shorten the delay
        delay -= 0.001

        #Icreasing the score
        score += 10

        if score > high_score:
            high_score = score

        mark.clear()
        mark.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal" ))


    #move the end portions to first in reverse order
    for index in range(len(portions)-1,0,-1):
        x=portions[index-1].xcor()
        y=portions[index-1].ycor()
        portions[index].goto(x,y)

    #move portion 0 to where the head is to be
    if len(portions)>0:
        x=shead.xcor()
        y=shead.ycor()
        portions[0].goto(x,y) 

    move()

    #check for head collision with the body portions
    for portion in portions:
        if portion.distance(shead)<20:
            time.sleep(1)
            shead.goto(0,0)
            shead.direction="stop"

            #hide the portions
            for portion in portions:
                portion.goto(1000,1000)
        
            #clear the portions
            portions.clear()

            #Reset the score
            score=0

            #Reset the delay
            delay=0.1

            #udate the score display
            mark.clear()
            mark.write("Score: {}  High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal" ))
    time.sleep(delay)

hs.mainloop()
2