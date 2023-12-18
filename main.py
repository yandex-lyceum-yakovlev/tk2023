import tkinter

def draw(event):
    canvas.create_oval((100, 100), (300, 300), fill='red')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
