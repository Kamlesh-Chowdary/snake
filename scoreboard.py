from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 18, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1

        self.update_score()
