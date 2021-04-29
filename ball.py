from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8)
        self.x_move = 3
        self.y_move = 3
        self.speed = 1
        self.random_move = [-1, 1]

    def move(self):
        new_x_pos = self.xcor() + self.x_move * self.speed
        new_y_pos = self.ycor() + self.y_move * self.speed

        self.goto(new_x_pos, new_y_pos)

    def y_collision(self):
        self.y_move *= -1
        self.x_move *= choice(self.random_move)

    def x_collision(self):
        self.x_move *= -1
        self.y_move *= choice(self.random_move)

    def reset_position(self):
        self.x_move *= choice(self.random_move)
        self.goto(0, 0)
