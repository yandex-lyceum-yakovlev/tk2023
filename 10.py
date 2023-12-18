import math
import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, bg='white', height=600, width=600)
points = []
x0 = y0 = r = 300
n = int(input())
if n < 7 and n != 5:
    print("Ошибка")
else:
    k = 0
    for i in range(2, (n + 1) // 2):
        if math.gcd(n, i) == 1:
            k = i
    print(k)
    t = 2 * math.pi / n
    for i in range(n + 1):
        dx = r * math.cos(t * i * k)
        dy = r * math.sin(t * i * k)
        points.append((int(x0 + dx), int(y0 + dy)))
    canvas.create_line(*points, fill='black')
    canvas.pack()
    window.mainloop()
