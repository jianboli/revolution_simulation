import tkinter as tk
import random
from digital_being import DigitalBeing
from environment import Environment

class SimulationApp:
    def __init__(self, root, width=40, height=40, cell_size=10):
        self.root = root
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas = tk.Canvas(root, width=width * cell_size, height=height * cell_size)
        self.canvas_offset = 2 
        self.canvas.pack()
        self.env = Environment(width=width, height=height)
        self.beings = [DigitalBeing(self.env, x=random.uniform(0, width), y=random.uniform(0, height)) for _ in range(20)]
        self.running = False
        self.env.generate_food(10)
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
            self.canvas_offset, self.canvas_offset,  # Top-left corner (slightly inset)
            self.width * self.cell_size+self.canvas_offset, self.height * self.cell_size + self.canvas_offset,  # Bottom-right corner (slightly inset)
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
        self.env.generate_food(5)
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

    def draw_beings(self, being):
        if being.is_alive():
            self.canvas.create_oval(
                    self.canvas_offset + being.x * self.cell_size, self.canvas_offset + being.y * self.cell_size,
                    self.canvas_offset + (being.x + being.size()) * self.cell_size, self.canvas_offset + (being.y + being.size()) * self.cell_size,
                    fill=f"#0000{int(255*being.percentage_hungry()):02x}",
                )
        else:
            self.canvas.create_oval(
                    self.canvas_offset + being.x * self.cell_size, self.canvas_offset + being.y * self.cell_size,
                    self.canvas_offset + (being.x + being.size()) * self.cell_size, self.canvas_offset + (being.y + being.size()) * self.cell_size,
                )
            self.canvas.create_text(
                self.canvas_offset + being.x * self.cell_size+10, self.canvas_offset + being.y * self.cell_size+10,
                fill="red",font="Times 20 italic bold", text="X")

            
    
    def draw_food(self, food):
        x, y = food
        self.canvas.create_oval(
                self.canvas_offset + x * self.cell_size, self.canvas_offset + y * self.cell_size,
                self.canvas_offset + (x + 0.5) * self.cell_size, self.canvas_offset + (y + 0.5) * self.cell_size,
                fill="green"
            )

    def draw_environment(self):
        """Draw the current state of the environment, including beings and food."""
        self.canvas.delete("all")  # Clear the canvas
        self.draw_boundary()  # Redraw the boundary
        
        for food in self.env.food_locations:
            self.draw_food(food)

        for being in self.beings:
            self.draw_beings(being)



if __name__ == "__main__":
    # Run the application
    root = tk.Tk()
    app = SimulationApp(root)

    root.mainloop()