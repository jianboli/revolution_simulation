from digital_being import DigitalBeing
from environment import Environment

if __name__ == "__main__":
    # Run the simulation
    initial_beings = [DigitalBeing() for _ in range(5)]
    env = Environment(food_availability=0.6)
    env.simulate(initial_beings, generations=10)