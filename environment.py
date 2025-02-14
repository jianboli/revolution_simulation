import random

# Simulation environment
class Environment:
    def __init__(self, food_availability=0.5):
        self.food_availability = food_availability

    def provide_food(self):
        return random.uniform(0, 1) < self.food_availability

    def simulate(self, beings, generations=10):
        for generation in range(generations):
            print(f"\n--- Generation {generation + 1} ---")
            new_beings = []
            for being in beings:
                if self.provide_food():
                    being.eat(5)  # Being finds food
                else:
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
