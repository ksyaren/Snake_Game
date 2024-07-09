import turtle
import random
import time

delay = 0.1
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
score_display.write("Score: 0   High Score: 0", align="center", font=("courier",21, "normal")) 

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
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y =head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y =head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#* keyboard's controls
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right,"Right")

#* Main Game loop
while True:
    wn.update()

    #! border controls
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # * hide the tail
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

        score =0
        delay =0.1

        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier",21, "normal"))

    #! eating controls
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #! adding new segments to tail
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment) 

        delay -=0.001
        score += 1


        if score > high_score:
            high_score =score

        score_display.clear()
        score_display.write("Score:{}  High Score: {}".format(score, high_score), align="center", font=("courier",21,"normal"))
    
    #* moving segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index -1].xcor()
        y= segments[index -1 ].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # * Tail bump checks
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            score =0 
            delay = 0.1


            score_display.clear()
            score_display.write("Score:{}  High Score: {}".format(score, high_score), align="center", font=("courier",21, "normal"))

    time.sleep(delay)

wn.mainloop