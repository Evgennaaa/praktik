import tkinter as tk
import time

m = tk.Tk()
m.title('Упругое столкновение')
m.geometry(f"300x600")
canvas = tk.Canvas(m, width=300, height=600, bg='#000',
                   highlightthickness=0)
canvas.pack()

width = 300
height = 600
radius = 20
yv = 0
x = width // 2
y = width // 2

oval_id = canvas.create_oval(x - radius, y - radius, x +
                             radius, y + radius, fill='grey', outline='white', width=3)

while True:
    yv += .5
    y += yv
    if y > height - 25:
        y = height - 25
        yv = -yv * .9
    time.sleep(0.02)
    canvas.coords(oval_id, x - radius, y - radius, x + radius,
                  y + radius)
    canvas.update()
