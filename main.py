import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Área de Terreno")
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.points = []
        self.image = None
        self.load_image()

        self.canvas.bind("<Button-1>", self.on_click)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((800, 600), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def on_click(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))

        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill='red')

        if len(self.points) > 1:
            self.canvas.create_line(self.points[-2], self.points[-1], fill='red')

        if len(self.points) > 2:
            self.calculate_area()

    def calculate_area(self):
        points = np.array(self.points)
        x = points[:, 0]
        y = points[:, 1]

        area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
        print(f"Área aproximada: {area} pixels²")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculator(root)
    root.mainloop()
