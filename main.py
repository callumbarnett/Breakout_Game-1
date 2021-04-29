from turtle import Screen
from block import Block
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from datetime import datetime, timedelta

global matrix_blocks, game_is_on, paddle, ball, scoreboard, screen_game


def create_game():
    global matrix_blocks, game_is_on, paddle, ball, scoreboard, screen_game

    screen_game = Screen()
    screen_game.title("Breakout Game")
    screen_game.setup(800, 400)
    screen_game.bgcolor("black")
    screen_game.tracer(0)

    paddle = Paddle()
    ball = Ball()
    scoreboard = Scoreboard()

    game_is_on = True
    matrix_blocks = []
    separation_blocks_y = 0
    colors_block = ["blue", "green", "yellow", "orange", "red"]

    for i in range(5):
        separation_blocks_x = 0
        if i % 2:
            cant_blocks = 13
            initial_x_pos = -330
        else:
            cant_blocks = 14
            initial_x_pos = -360

        blocks = []
        for j in range(cant_blocks):
            blocks.append(Block(color=colors_block[i],
                                position=(initial_x_pos + separation_blocks_x, 40 + separation_blocks_y)))
            separation_blocks_x += 55
        matrix_blocks.append(blocks)
        separation_blocks_y += 26


def play_game():
    global game_is_on

    screen_game.listen()
    screen_game.onkeypress(paddle.go_right, "Right")
    screen_game.onkeypress(paddle.go_left, "Left")
    screen_game.onkey(reset_game, "r")

    # Increment speed every 10 seconds
    actual_time = datetime.now()
    next_speed_increment = actual_time + timedelta(seconds=10)

    while game_is_on:
        screen_game.update()
        ball.move()

        # Collision with any block
        level_blocks = 20
        for list_blocks in matrix_blocks:
            for block in list_blocks:
                if ball.distance(block) < 35 and ball.ycor() > level_blocks:
                    block.hideturtle()
                    list_blocks.remove(block)
                    ball.y_collision()
                    scoreboard.add_score(int((level_blocks - 20) / 26 + 1))
            level_blocks += 26

        # Collision with Walls
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.x_collision()

        # Collision with paddle or collision with the up wall
        if (ball.distance(paddle) < 61.5 and ball.ycor() < -135) or (ball.ycor() > 190):
            ball.y_collision()

        # If the ball go down below the screen, then the game end
        if ball.ycor() < -210:
            ball.reset_position()
            scoreboard.game_over()
            game_is_on = False
            if scoreboard.score > scoreboard.high_score:
                scoreboard.update_high_score()

        actual_time = datetime.now()
        if actual_time > next_speed_increment:
            next_speed_increment = actual_time + timedelta(seconds=10)
            ball.speed += 0.4
            print(ball.speed)


def game():
    create_game()
    play_game()


def reset_game():
    screen_game.clear()
    game()


game()

screen_game.exitonclick()
