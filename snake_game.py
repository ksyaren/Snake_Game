import turtle
import random
import time

delay = 0.5
score = 0
high_score = 0

# * create the screen 
# ! wn represents the graphic display 

wn = turtle.screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width = 600, height= 600)
wn.tracer(0)   # ! This will stop the screen from updating automatically

# * head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0) # * snake stops in the middle of the screen
head.direction = "stop"
