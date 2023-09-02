import turtle as t
import snake as s
import random as r

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class AltSnake(s.Snake):
    def __init__(self):
        super().__init__()

    def square_colour(self):
        red = r.random()
        green = r.random()
        blue = r.random()

        colour = (red, green, blue)

        return colour

    def add_square(self, position):
        new_square = t.Turtle(shape="circle")
        new_square.color(self.square_colour())
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def shrink(self):
        for square in self.squares[10:]:
            square.ht()
        self.squares = self.squares[:10]