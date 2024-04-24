from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_DIRECTIONS = ["left", "right"]

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance != 1:
            return None

        direction = random.choice(START_DIRECTIONS)

        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color("black", random.choice(COLORS))
        x_pos = 300 if direction == "right" else -300
        y_pos = random.randrange(-250, 250, 10)
        new_car.goto(x_pos, y_pos)
        new_car.setheading(180 if direction == "right" else 0)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT

        for car in self.cars:
            car.hideturtle()
        self.cars = []
