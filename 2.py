import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, bg='white', height=600, width=600)
for x in range(3, 600, 74):
    canvas.create_line((x, 3), (x, 595), fill='black')
    canvas.create_line((3, x), (595, x), fill='black')
canvas.pack()
window.mainloop()
