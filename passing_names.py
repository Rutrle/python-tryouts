from tkinter import *
from tkinter import messagebox, ttk


class whatever:
    def __init__(self):
        root = Tk()
        root.title('Cycle plotter')
        my_notebook = ttk.Notebook(root)
        my_notebook.pack()
        self.frame_creator('frame_one', my_notebook, 'text_one')
        self.frame_creator('frame_two', my_notebook, 'text_two')

        root.mainloop()

    def frame_creator(self, frame_name, master_frame, text):
        self.frame_name = Frame(master_frame, width=500, height=500)
        self.frame_name.pack(fill='both', expand=1)
        master_frame.add(self.frame_name, text=text)


if __name__ == "__main__":
    whatever()
