import tkinter


def key_pressed(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    if event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    x = canvas.coords(oval)[0] % 600
    y = canvas.coords(oval)[1] % 600
    canvas.coords(oval, (x, y, x + 10, y + 10))


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()