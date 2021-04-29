from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 0)

        self.high_score = 0
        self.score = 0

        self.get_high_score()
        self.update_score()

    def get_high_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.readline())

    def update_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.score))
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-130, 160)
        self.write(f"High score: {self.high_score}", font=("Courier", 20, "normal"), align="right")
        self.goto(200, 160)
        self.write(f"Score: {self.score}", font=("Courier", 20, "normal"), align="left")

    def add_score(self, points):
        self.score += points
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", font=("Courier", 80, "normal"), align="center")
        self.goto(0, -70)
        self.write(f"Press R to play again", font=("Courier", 30, "normal"), align="center")
