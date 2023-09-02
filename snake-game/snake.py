import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def grow_snake(self, growth):
        for _ in range(growth + 1):
            new_square_position = self.squares[-1].position()
            self.add_square(new_square_position)

    def add_square(self, position):
        new_square = t.Turtle(shape="square")
        new_square.color("purple")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def move(self):
        for square in range(len(self.squares) - 1, 0, - 1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def wall_collision(self):
        if self.head.xcor() < -290:
            return True
        elif self.head.xcor() > 290:
            return True
        elif self.head.ycor() > 290:
            return True
        elif self.head.ycor() < -290:
            return True
        else:
            return False

    def tail_collision(self):
        for square in self.squares[1:]:
            if self.head.distance(square) < 10:
                return True
