import random
import math

# Simulation environment
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
            print(f"Food generated at ({food_x:.2f}, {food_y:.2f})")

    def provide_food(self, being):
        for food in self.food_locations[:]:
            food_x, food_y = food
            if math.sqrt((being.x - food_x)**2 + (being.y - food_y)**2) < 1:  # Being is close enough to eat
                being.eat(5)
                self.food_locations.remove(food)
                return True
        return False

    def simulate(self, beings, generations=10):
        for generation in range(generations):
            print(f"\n--- Generation {generation + 1} ---")
            self.generate_food()
            new_beings = []
            for being in beings:
                being.move()
                if not self.provide_food(being):
                    print("Being found no food.")

                being.metabolize()

                if being.is_alive():
                    if being.can_reproduce():
                        child = being.reproduce()
                        if child:
                            new_beings.append(child)
                    new_beings.append(being)
                else:
                    print("Being has died.")

            beings = new_beings
            print(f"Population size: {len(beings)}")
            for being in beings:
                print(being)

