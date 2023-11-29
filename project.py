from tkinter import *
from ttkthemes import ThemedTk

root = Tk()
root.title("Basic understanding")
root.geometry('500x500')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

lbl = Label(root, text="Widgets")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)


def clicked():
    if txt.get():
        res = "Button is Clicked your text is " + txt.get()
        lbl.configure(text=res)
    else:
        res = "You have to enter something"
        lbl.configure(text=res)


btn = Button(root, text="Click me", fg="red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()
