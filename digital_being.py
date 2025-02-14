import random

class DigitalBeing:
    def __init__(self, energy=10, age=0, reproduction_age=5, mutation_rate=0.1):
        self.energy = energy
        self.age = age
        self.reproduction_age = reproduction_age
        self.mutation_rate = mutation_rate
        self.genetic_trait = random.uniform(0, 1)  # A trait that affects survival and reproduction

    def eat(self, food):
        self.energy += food
        print(f"Being ate {food} energy. Current energy: {self.energy}")

    def metabolize(self):
        self.energy -= 1
        self.age += 1
        print(f"Being metabolized. Current energy: {self.energy}, Age: {self.age}")

    def is_alive(self):
        return self.energy > 0

    def can_reproduce(self):
        return self.age >= self.reproduction_age

    def reproduce(self):
        if self.can_reproduce():
            print("Being is reproducing!")
            # Create a new being with inherited traits, possibly mutated
            child_trait = self.genetic_trait + random.uniform(-self.mutation_rate, self.mutation_rate)
            child_trait = max(0, min(1, child_trait))  # Ensure trait stays within bounds
            child = DigitalBeing(energy=10, age=0, reproduction_age=self.reproduction_age, mutation_rate=self.mutation_rate)
            child.genetic_trait = child_trait
            self.energy -= 5  # Cost of reproduction
            return child
        else:
            print("Being is too young to reproduce.")
            return None

    def __str__(self):
        return f"DigitalBeing(energy={self.energy}, age={self.age}, genetic_trait={self.genetic_trait:.2f})"
