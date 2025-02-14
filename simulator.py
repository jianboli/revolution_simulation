import tkinter as tk
import random
from digital_being import DigitalBeing
from environment import Environment

class SimulationApp:
    def __init__(self, root, width=10, height=10, cell_size=40):
        self.root = root
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas = tk.Canvas(root, width=width * cell_size, height=height * cell_size)
        self.canvas.pack()
        self.env = Environment(width=width, height=height)
        self.beings = [DigitalBeing(x=random.uniform(0, width), y=random.uniform(0, height)) for _ in range(5)]
        self.running = False
        self.setup_controls()

    def setup_controls(self):
        self.start_button = tk.Button(self.root, text="Start", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_simulation)
        self.stop_button.pack(side=tk.LEFT)
        
    def draw_boundary(self):
        """Draw a rectangle to represent the boundary of the environment."""
        # Adjust coordinates to ensure the boundary is fully visible
        self.canvas.create_rectangle(
            2, 2,  # Top-left corner (slightly inset)
            self.width * self.cell_size - 2, self.height * self.cell_size - 2,  # Bottom-right corner (slightly inset)
            outline="black", width=2
        )

    def start_simulation(self):
        self.running = True
        self.run_simulation()

    def stop_simulation(self):
        self.running = False

    def run_simulation(self):
        if not self.running:
            return
        self.env.generate_food()
        new_beings = []
        for being in self.beings:
            being.move()
            self.env.provide_food(being)
            being.metabolize()
            if being.is_alive():
                if being.can_reproduce():
                    child = being.reproduce()
                    if child:
                        new_beings.append(child)
                new_beings.append(being)
        self.beings = new_beings
        self.draw_environment()
        self.root.after(500, self.run_simulation)  # Run every 500ms

    def draw_environment(self):
        """Draw the current state of the environment, including beings and food."""
        self.canvas.delete("all")  # Clear the canvas
        self.draw_boundary()  # Redraw the boundary
        
        for food in self.env.food_locations:
            x, y = food
            self.canvas.create_oval(
                x * self.cell_size, y * self.cell_size,
                (x + 0.5) * self.cell_size, (y + 0.5) * self.cell_size,
                fill="green"
            )
        for being in self.beings:
            self.canvas.create_oval(
                being.x * self.cell_size, being.y * self.cell_size,
                (being.x + 0.5) * self.cell_size, (being.y + 0.5) * self.cell_size,
                fill="blue"
            )

if __name__ == "__main__":
    # Run the application
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()