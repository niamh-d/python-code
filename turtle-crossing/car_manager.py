import turtle as t
import random as r

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [280, 240, 200, 160, 120, 80, 40, 0, -40, -80, -120, -160, -200, -240, -280]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()

        self.create_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(r.choice(COLOURS))
        self.penup()
        self.goto(280, r.choice(Y_POSITIONS))
        self.setheading(180)

    def move(self):
        self.fd(STARTING_MOVE_DISTANCE)

