import numpy as np
import environment

class DigitalBeing:
    def __init__(self, env, energy=90, age=0, mutation_rate=0.1, x=0, y=0):
        self._energy = energy
        self.age = age
        self.mutation_rate = mutation_rate
        self.genetic_trait = np.random.uniform(0, 1)
        self.x = x
        self.y = y
        self.model_weights = np.random.rand(2)  # Simple model: weights for x and y directions
        self.env = env
        
        self.hungry_bar = 50
        self.full_bar = 90
        self.max_energy = 100
        
        self.initial_size = 1
        self.grownup_size = 5
        
        self.grownup_age = 5
        self.reproduce_probability = 0.5

    @property
    def energy(self):
        return self._energy
    
    @energy.setter
    def energy(self, val):
        if self._energy == 0:
            return # dead, cannot set a value anymore
        self._energy = max([0, val]) # make sure it is not negative

    def eat(self, food):
        if not self.is_alive:
            return False
        
        if self.energy == self.max_energy:
            return False
        else:
            self.energy += food
            return True

    def size(self):
        return (self.grownup_size - self.initial_size) * (min([self.grownup_age, self.age]))/self.grownup_age + self.initial_size

    def percentage_hungry(self):
        return self.energy / self.max_energy

    def metabolize(self):
        if self.is_alive():
            self.energy -= 1
            self.age += 1

    def is_alive(self):
        return self.energy > 0

    def can_reproduce(self):
        return self.is_alive and self.age >= self.grownup_age and self.energy > self.full_bar 

    def reproduce(self):
        if self.can_reproduce():
            if np.random.rand() < self.reproduce_probability:
                child = DigitalBeing(self.env, energy=50, age=0, mutation_rate=self.mutation_rate, x=self.x, y=self.y)
                child.model_weights = self.model_weights + self.mutation_rate * np.random.randn(2)  # Mutate weights
                self.energy -= 50  # Cost of reproduction
                return child
        return None
    
    def predict_direction(self):
        """Predict the best direction to move based on the model."""
        if self.energy < self.hungry_bar:
            d = self.model_weights + np.random.randn(2) * 0.1
            return d/np.linalg.norm(d)  # Normalize to get a unit vector
        elif self.energy > self.full_bar:
            d = -self.model_weights + np.random.randn(2) * 0.1
            return d/np.linalg.norm(d)  # Normalize to get a unit vector 
        else:
            d = np.random.rand(2)
            return d / np.linalg.norm(d)

    def update_model(self, food_found):
        """Update the model weights based on whether food was found."""
        if food_found:
            # Reinforce the current direction
            self.model_weights += 0.1 * np.random.rand(2)
        else:
            # Explore a new direction
            self.model_weights -= 0.1 * np.random.rand(2)

    def move(self, max_step=1):
        """Move in the predicted direction."""
        if not self.is_alive:
            return 
        
        direction = self.predict_direction()
        self.x += direction[0] * max_step
        self.y += direction[1] * max_step
        # Ensure the being stays within the environment boundaries
        self.x = max(0, min(self.x, self.env.width))
        self.y = max(0, min(self.y, self.env.height))

