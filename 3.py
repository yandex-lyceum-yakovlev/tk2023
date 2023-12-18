import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, bg='white', height=600, width=600)
w = 74
for x in range(3, 600, w):
    canvas.create_line((x, 3), (x, 3 + w * 8), fill='black')
    canvas.create_line((3, x), (3 + w * 8, x), fill='black')
for i in range(8):
    for j in range(8):
        x = 3 + j * w
        y = 3 + i * w
        if (i < 3 or i > 4) and ((i + j) % 2 == 0):
            if i < 3:
                color = "red"
            else:
                color = "blue"
            canvas.create_oval((x, y), (x + w, y + w), fill=color)
canvas.pack()
window.mainloop()
