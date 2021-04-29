from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=7)
        self.goto(0, -150)

    def go_right(self):
        new_x_cor = self.xcor() + 20
        self.goto(new_x_cor, self.ycor())

    def go_left(self):
        new_x_cor = self.xcor() - 20
        self.goto(new_x_cor, self.ycor())
