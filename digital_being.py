import tkinter as tk
import random
import math

class DigitalBeing:
    def __init__(self, energy=10, age=0, reproduction_age=5, mutation_rate=0.1, x=0, y=0):
        self.energy = energy
        self.age = age
        self.reproduction_age = reproduction_age
        self.mutation_rate = mutation_rate
        self.genetic_trait = random.uniform(0, 1)
        self.x = x
        self.y = y

    def eat(self, food):
        self.energy += food

    def metabolize(self):
        self.energy -= 1
        self.age += 1

    def is_alive(self):
        return self.energy > 0

    def can_reproduce(self):
        return self.age >= self.reproduction_age

    def reproduce(self):
        if self.can_reproduce():
            child_trait = self.genetic_trait + random.uniform(-self.mutation_rate, self.mutation_rate)
            child_trait = max(0, min(1, child_trait))
            child = DigitalBeing(energy=10, age=0, reproduction_age=self.reproduction_age, mutation_rate=self.mutation_rate, x=self.x, y=self.y)
            child.genetic_trait = child_trait
            self.energy -= 5
            return child
        return None

    def move(self, max_step=1):
        self.x += random.uniform(-max_step, max_step)
        self.y += random.uniform(-max_step, max_step)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
