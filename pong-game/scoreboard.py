import turtle as t

FONT = ("Courier", 80, "normal")

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score= 0
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.write_scores()

    def r_point(self):
        self.r_score += 1
        self.write_scores()
