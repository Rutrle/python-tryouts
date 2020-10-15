from tkinter import *
from tkinter import messagebox, ttk


class whatever:
    def __init__(self):
        root = Tk()
        root.title('Cycle plotter')
        my_notebook = ttk.Notebook(root)
        my_notebook.pack()

        self.frame_manual = Frame(my_notebook, width=500, height=500)
        self.frame_manual.pack(fill='both', expand=1)
        print(type(self.frame_manual))
        print(self.frame_manual)
        print(self.frame_manual.)
        my_notebook.add(self.frame_manual, text='manual frame')

        self.frame_creator('frame_one', my_notebook, 'text_one')
        self.frame_creator('frame_two', my_notebook, 'text_two')

        label_one = Label(self.frame_two, text="I'm a label")
        label_one.pack()

        root.mainloop()

    def frame_creator(self, frame_name, master_frame, text):
        self.frame_name = Frame(master_frame, width=500, height=500)
        self.frame_name.pack(fill='both', expand=1)
        print(type(self.frame_name))
        print(self.frame_name)
        master_frame.add(self.frame_name, text=text)


if __name__ == "__main__":
    whatever()
