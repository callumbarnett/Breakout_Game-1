from turtle import Turtle


class Block(Turtle):
    def __init__(self, color="black", position=(0, 0)):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(position)
