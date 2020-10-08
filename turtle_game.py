#turtle graphics game
import turtle
import random
import math
import time

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.color("white")
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)

mypen.hideturtle()

# goal
maxgoals = 5
goals = []

for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].penup()
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300), random.randint(-300,300))

#create player turtle
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)

# set speed variable
speed = 3
score = 0

# dfine functions
def turnleft():
    player.left(90)

def turnright():
    player.right(90)

def increasespeed():
    global speed
    speed+= 1

def stay():
    global speed
    speed = 0

def decreasespeed():
    global speed
    speed-= 1

def toexit():
    turtle.bye()

def iscollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()- t2.xcor(),2) + math.pow(t1.ycor()- t2.ycor(),2))
    if d < 20:
        return True
turtle.listen()
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(stay,"s")
turtle.onkey(increasespeed,"i")
turtle.onkey(decreasespeed,"d")
turtle.onkey(toexit,"Escape")
flag = 1
diff = 0
sec1 = int(time.strftime("%S",time.localtime()))
min1 = int(time.strftime("%M",time.localtime()))
while flag:
    min2 = int(time.strftime("%M",time.localtime()))
    sec2 = int(time.strftime("%S",time.localtime()))
    if min1 != min2:
        sec1 = sec1 - 60
    diff = sec2 - sec1
    if diff == 35:
        turtle.bye()
        print(score)
      #  flag = 0
        
    player.forward(speed)
    #check boundry conditions for player
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)

    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        
    #set boundary condition for goal
    for count in range(maxgoals):
        if goals[count].xcor() > 290 or goals[count].xcor() <-290:
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() <-290:
            goals[count].right(180)
        
        if iscollision(player,goals[count]):
            goals[count].setposition(random.randint(-290,290), random.randint(-290,290))
            goals[count].right(random.randint(0,360))
            score+=1
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            scorestring = "Score : {}".format(score)
            mypen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
        # move goal
        goals[count].forward(2)




