import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Love You  mummy 💖")

# Heart drawing turtle
heart = turtle.Turtle()
heart.pensize(3)
heart.color("red")
heart.speed(0)
heart.hideturtle()

# Text turtle
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("purple")

# Star decoration turtle
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)

# Gift box turtle
gift = turtle.Turtle()
gift.hideturtle()
gift.pensize(2)

# Function to draw heart
def draw_heart():
    heart.penup()
    heart.goto(0, -100)
    heart.pendown()
    heart.begin_fill()
    heart.fillcolor("red")
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()
    heart.setheading(0)

# Function to blink heart
def blink_heart(times):
    for _ in range(times):
        heart.clear()
        time.sleep(0.3)
        draw_heart()
        time.sleep(0.3)

# Function to write message
def write_message():
    text.goto(0, 100)
    text.write("Love You mummy 💖", align="center", font=("Arial", 24, "bold"))

# Function to draw a star
def draw_star(x, y):
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    stars.color(random.choice(["pink", "orange", "skyblue", "gold"]))
    stars.begin_fill()
    for _ in range(5):
        stars.forward(20)
        stars.right(144)
    stars.end_fill()

# Function to draw gift box
def draw_gift():
    gift.penup()
    gift.goto(-40, -200)
    gift.pendown()
    gift.fillcolor("hotpink")
    gift.begin_fill()
    for _ in range(2):
        gift.forward(80)
        gift.left(90)
        gift.forward(60)
        gift.left(90)
    gift.end_fill()

    # Ribbon
    gift.penup()
    gift.goto(0, -200)
    gift.setheading(90)
    gift.pendown()
    gift.color("yellow")
    gift.forward(60)

# Run all parts
draw_heart()
write_message()
for _ in range(20):
    draw_star(random.randint(-200, 200), random.randint(-50, 200))
draw_gift()
blink_heart(5)

turtle.done()