import numpy as np

class DigitalBeing:
    def __init__(self, energy=10, age=0, reproduction_age=5, mutation_rate=0.1, x=0, y=0):
        self.energy = energy
        self.age = age
        self.reproduction_age = reproduction_age
        self.mutation_rate = mutation_rate
        self.genetic_trait = np.random.uniform(0, 1)
        self.x = x
        self.y = y
        self.model_weights = np.random.rand(2)  # Simple model: weights for x and y directions


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
            child = DigitalBeing(energy=10, age=0, reproduction_age=self.reproduction_age, mutation_rate=self.mutation_rate, x=self.x, y=self.y)
            child.model_weights = self.model_weights + self.mutation_rate * np.random.randn(2)  # Mutate weights
            self.energy -= 5  # Cost of reproduction
            return child
        return None
    
    def predict_direction(self):
        """Predict the best direction to move based on the model."""
        return self.model_weights / np.linalg.norm(self.model_weights)  # Normalize to get a unit vector

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
        direction = self.predict_direction()
        self.x += direction[0] * max_step
        self.y += direction[1] * max_step
        # Ensure the being stays within the environment boundaries
        self.x = max(0, min(self.x, self.env.width))
        self.y = max(0, min(self.y, self.env.height))

