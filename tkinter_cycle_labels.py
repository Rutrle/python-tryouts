from tkinter import *

k = []
root = Tk()
for i in range(10):
    k.append(Label(root, text=f'label{i}'))
    k[i].grid(row=i, column=i)

root.mainloop()
