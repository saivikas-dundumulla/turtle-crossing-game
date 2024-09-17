import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_mngr = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_mngr.create_car()
    car_mngr.move_all_cars()

    # detect the collision with any cars
    for car in car_mngr.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when the car reaches other side
    if player.ycor() > 280:
        scoreboard.increase_lvl()
        car_mngr.increase_lvl()
        player.reset()

screen.exitonclick()