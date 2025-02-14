import random
import math

class Environment:
    def __init__(self, food_availability=0.5, width=10, height=10):
        self.food_availability = food_availability
        self.width = width
        self.height = height
        self.food_locations = []

    def generate_food(self):
        if random.uniform(0, 1) < self.food_availability:
            food_x = random.uniform(0, self.width)
            food_y = random.uniform(0, self.height)
            self.food_locations.append((food_x, food_y))

    def provide_food(self, being):
        for food in self.food_locations[:]:
            food_x, food_y = food
            if math.sqrt((being.x - food_x)**2 + (being.y - food_y)**2) < 1:
                being.eat(5)
                self.food_locations.remove(food)
                return True
        return False