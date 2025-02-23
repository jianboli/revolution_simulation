import numpy as np

class Environment:
    def __init__(self, food_availability=0.5, width=10, height=10):
        self.food_availability = food_availability
        self.width = width
        self.height = height
        self.food_locations = []

    def _clip_food(self,x, m):
        if x < 0:
            x = 0
        if x > m:
            x = m
        return x

    def generate_food(self, n=1):
        # Let's only generate food at some place
        for _ in range(n):
            if np.random.uniform(0, 1) < self.food_availability:
                food_x = int(np.random.randn()*self.width/5+self.width/3)
                food_y = int(np.random.randn()*self.width/5+self.height/3)
                food_x = self._clip_food(food_x, self.width)
                food_y = self._clip_food(food_y, self.height)
                
                self.food_locations.append((food_x, food_y))

    def provide_food(self, being):
        for food in self.food_locations[:]:
            food_x, food_y = food
            if np.sqrt((being.x - food_x)**2 + (being.y - food_y)**2) < 1:  # Being is close enough to eat
                if being.eat(5):
                    self.food_locations.remove(food)
                being.update_model(food_found=True)  # Update model with positive feedback
                return True
        being.update_model(food_found=False)  # Update model with negative feedback
        return False