import turtle as t
import random as r


class Potion(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white", "blue")
        self.speed(0)
        self.be_placed()

    def be_placed(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 265)
        self.goto(random_x, random_y)

