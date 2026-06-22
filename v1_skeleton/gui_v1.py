from tkinter import *
from tkinter.ttk import *



class shape:
    def __init__(self, root=None):
        self.root = root

        self.create()
    
    def create(self):

        self.canvas  = Canvas(self.root)

        self.canvas.create_rectangle(10, 10, 320, 60,
                                     outline = "black", fill = "white",
                                     width = 3.5)
        self.canvas.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    shape = shape(root)
    root.title("Advisory")
    
    root.geometry("330x220+300+300")

mainloop() 