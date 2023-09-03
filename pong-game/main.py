import turtle as t
import paddle as p
import ball as b
import scoreboard as s
import dividing_line as dl
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = p.Paddle((340, 0))
l_paddle = p.Paddle((-340, 0))
ball = b.Ball()
scoreboard = s.Scoreboard()
dividing_line = dl.DividingLine()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()
        time.sleep(0.5)

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()
        time.sleep(0.5)


screen.exitonclick()
