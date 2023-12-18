import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, bg='white', height=600, width=600)
canvas.create_rectangle((100, 100), (300, 400), fill='blue')
canvas.create_oval((100, 100), (300, 400), fill='yellow')
canvas.create_line((100, 100), (300, 400), fill='red')
canvas.pack()
window.mainloop()

