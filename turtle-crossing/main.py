import time
import turtle as t
import player as p
import car_manager as cm
import scoreboard as s

screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = p.Player()

car_manager = cm.CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager = cm.CarManager()
    car_manager.move()
