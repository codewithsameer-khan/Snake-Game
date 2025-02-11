
# snake Game by using Turtle module


from turtle import Turtle,Screen
import time
import random

# Screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
# Screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")


screen.tracer(0)

# Welcome message
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("red")
writer.goto(0, 260)
writer.write("Welcome to Snake Game!", align="center", font=("Arial", 24, "normal"))

# Snake setup
snake_segments = []
initial_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in initial_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake_segments.append(segment)

snake_head = snake_segments[0]

# Movement functions
def up():
    if snake_head.heading() != 270: 
        snake_head.setheading(90)

def down():
    if snake_head.heading() != 90:
        snake_head.setheading(270)

def left():
    if snake_head.heading() != 0:
        snake_head.setheading(180)

def right():
    if snake_head.heading() != 180:
        snake_head.setheading(0)

# Key bindings
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# Food setup
food = Turtle()
food.shape("circle")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.color("blue")
food.speed("fastest")
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Scoreboard setup
score_value = 0
score = Turtle()
score.color("white")
score.penup()
score.goto(0, 270)
score.hideturtle()
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
score.write(f"Score: {score_value}", align=ALIGNMENT, font=FONT)

# Move the snake
def move():
    for idx in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[idx - 1].xcor()
        new_y = snake_segments[idx - 1].ycor()
        snake_segments[idx].goto(new_x, new_y)
    snake_head.forward(20)

# Game loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    move()
    
    # Detect collision with food
    if snake_head.distance(food) < 20:
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        food.goto(random_x, random_y)
        
        # Add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        snake_segments.append(new_segment)
        
        # Update score
        score_value += 1
        score.clear()
        score.write(f"Score: {score_value}", align=ALIGNMENT, font=FONT)
    
    # Detect collision with wall
    if (
        snake_head.xcor() > 280 or snake_head.xcor() < -280 or 
        snake_head.ycor() > 280 or snake_head.ycor() < -280
    ):
        is_game_on = False
        score.goto(0, 0)
        score.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    # Detect collision with itself
    for segment in snake_segments[1:]:
        if snake_head.distance(segment) < 10:
            is_game_on = False
            score.goto(0, 0)
            score.write("GAME OVER", align=ALIGNMENT, font=FONT)

screen.exitonclick()