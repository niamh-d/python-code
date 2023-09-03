import turtle as t


class DividingLine(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        while self.ycor() > -290:
            self.fd(10)
            self.pendown()
            self.fd(10)
            self.penup()