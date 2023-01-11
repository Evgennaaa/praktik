import tkinter as tk
from math import cos, sin, radians

root = tk.Tk()
root.geometry("600x600")

canvas = tk.Canvas(root, background="white")
canvas.pack(fill="both", expand=True)


def create_circle(x, y, r, canvasName):
    id = canvas.create_oval(x-r, y-r, x+r, y+r)
    return id


def move(angle):
    if angle >= 360:
        angle = 0
    x = 300 + cos(radians(angle))*250
    y = 300 + sin(radians(angle))*250
    angle += 1
    canvas.coords(point, x, y, x, y)
    root.after(10, move, angle)


create_circle(300, 300, 200, 'canvas')
point = canvas.create_oval(294, 44, 304, 54, fill='black')

root.after(10, move, 0)

root.mainloop()
