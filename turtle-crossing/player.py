import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.move_to_start()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def move_to_start(self):
        self.goto(STARTING_POSITION)

