import turtle
import time
import random

WIDTH, HEIGHT = 800, 800
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan', 'grey']

def get_turtle_numb():
    turtles = 0
    while True:
        turtles = input('Enter the number of turtles (2-11): ')
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print('Input invalid, try again.')
            continue
        if 2 <= turtles <= 11:
            return turtles
        else:
            print('Number of turtles is not in range, try again.')

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            dist = random.randrange(1,20)
            racer.forward(dist)

            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Ultimate turtle racing championship')

turtles = get_turtle_numb()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:turtles]

winner = race(colors)
print(f"The winner is the {winner} turtle")
time.sleep(2)
