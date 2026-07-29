import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
from tkinter import *
import subprocess
#title of window
root.title("Advisory")

canvas = tk.Canvas(root, width=600, height=100)
canvas.grid(columnspan=3)

#logo

#...

#welcoming
welcoming = tk.Label(root, text="Specifics:", font="Raleway")
welcoming.grid(columnspan=3, column=0, row=1)


def show():  
    lbl.config(text=opt.get())

# Dropdown options  
types = ["General", "Relationship", "Financial", "Academic", "Career", "Entertainment"]  

# Selected option variable  
opt = StringVar(value="General")  

# Dropdown menu  
OptionMenu(root, opt, *types).grid()  

# Button to update label  
Button(root, text="Confirm", command=show).grid()  

lbl = Label(root, text=" ")  
lbl.grid()  




def on_ok():
    subprocess.Popen(['python', 'SkeletonV2/main_version2.py'])
    root.destroy()
   

def on_cancel():
    root.destroy()

button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="Back", width=10, command=on_ok).grid(row=7, column=0, padx=5)

root.mainloop()