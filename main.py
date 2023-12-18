import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, bg='blue', height=600, width=600)
canvas.create_line((0, 0), (600, 600), fill='red')
canvas.pack()
window.mainloop()

