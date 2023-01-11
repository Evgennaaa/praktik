from tkinter import *
from random import randint

root = Tk()

t = Canvas(width=800, height=600, bg='#D3D3D3')

drops = []

t.pack()


class drop:
    def __init__(self):
        self._x = randint(5, 795)
        self._avatar = t.create_line(
            self._x, 1, self._x, 5, fill='#000080')
        self._y = 0

        self._v = 10

    def fly(self):
        self._y += self._v
        t.coords(self._avatar, self._x, self._y, self._x, self._y+10)


def sky():
    a = randint(1, 6)
    drops.extend([drop() for i in range(a)])
    t.after(100, sky)


def mov():
    for drop in drops:
        drop.fly()
    t.after(25, mov)


sky()
mov()

root.mainloop()
