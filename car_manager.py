import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 8)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.setheading(180)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_all_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_lvl(self):
        self.car_speed += MOVE_INCREMENT