import tkinter
import random


def draw(event):
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    d = random.randint(0, 100)
    canvas.create_oval((x1, y1), (x1 + d, y1 + d), fill='red')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
