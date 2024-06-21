from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 21, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)


    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 21, 'normal'))
