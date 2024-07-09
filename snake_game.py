import turtle
import random
import time

delay = 0.5
score = 0
high_score = 0

# * create the screen 
# ! wn represents the graphic display 

wn = turtle.Screen() 
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width = 600, height= 600)
wn.tracer(0)   # ! This will stop the screen from updating automatically

# * head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0) # * snake stops in the middle of the screen
head.direction = "stop"

# * snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# * snake segments
segments = [] 

# * pen for the score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0,260) 
score_display.write("Score: 0   High Score: 0", align="center", font=("courier",24, "normal")) 

# * functions

def go_up():
    if head.direction != "down":
        head.direction ="up"

def go_down():
    if head.direction != "up":
        head.direction ="down"

def go_left():
    if head.direction != "right":
        head.direction ="left"

def go_right():
    if head.direction !="left":
        head.driection = "right"

def move():
    if head.direction == "up":
        y =head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y =head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    