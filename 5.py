import tkinter


def show_key(event):
    label.config(text=(event.keysym, event.char, event.keysym_num,event.keycode))


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()