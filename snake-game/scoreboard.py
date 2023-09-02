import turtle as t
import mine as m

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
        if self.score == 10 or self.score == 15 or self.score == 35 or self.score == 40:
            mine = m.Mine()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("pink")
        self.write(f"GAME OVER! Your final score: {self.score}", move=False, align=ALIGNMENT, font=FONT)