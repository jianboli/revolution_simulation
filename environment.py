import numpy as np

class Environment:
    def __init__(self, food_availability=0.5, width=10, height=10):
        self.food_availability = food_availability
        self.width = width
        self.height = height
        self.food_locations = []

    def generate_food(self):
        if np.random.uniform(0, 1) < self.food_availability:
            food_x = np.random.uniform(0, self.width)
            food_y = np.random.uniform(0, self.height)
            self.food_locations.append((food_x, food_y))

    def provide_food(self, being):
        for food in self.food_locations[:]:
            food_x, food_y = food
            if np.sqrt((being.x - food_x)**2 + (being.y - food_y)**2) < 1:  # Being is close enough to eat
                being.eat(5)
                being.update_model(food_found=True)  # Update model with positive feedback
                self.food_locations.remove(food)
                return True
        being.update_model(food_found=False)  # Update model with negative feedback
        return False