import tkinter as tk
import subprocess
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
#title of window
root.title("Advisory")
#import customtkinter as ctk
#import tkinter.messagebox as tkmb

#notes
'''root.state("zoomed")'''

'''# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")'''

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

#logo
logo = Image.open('SkeletonV2/images/Advisory_logo.png')
res = logo.resize((300, 300), Image.Resampling.LANCZOS)
#notes:
'''logo = Image.open('SkeletonV2/images/Advisory_logo.png').resize((size[0], size[1]), Image.Resampling.LANCZOS)
#LANCZOS allows images to be resized'''

logo = ImageTk.PhotoImage(res)
#logo in label
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#welcoming
welcoming = tk.Label(root, text="Welcome to Advisory! Enter your desired type of advise and we'll be right with you!", font="Raleway")
welcoming.grid(columnspan=3, column=0, row=1)

# Tkinter string variable
# able to store any string value
v = StringVar(root, "1")

# --- Radio buttons (Notification) ---
tk.Label(root, text="Select Choice:").grid(row=4, column=0, columnspan=2)
advice = tk.StringVar(value="Ask Advice")
advice_list = ["Ask Advice", "Add Advice"]
advice_frame = tk.Frame(root)
advice_frame.grid(row=5, column=0, columnspan=2)
for d in advice_list:
    tk.Radiobutton(advice_frame, text=d, variable=advice, value=d).pack(anchor="w")
#notes:
'''# Dictionary to create multiple buttons
values = {"Financial" : "1",
        "Relationship" : "2",
        "Career" : "3",
        "General" : "4"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v, 
                value = value, indicator = 0,
                width=40,
                background = "lightblue",).grid(columnspan=3, ipady=4)'''

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())

#continue to next page button

# --- Command buttons ---
def on_ok():
    subprocess.Popen(['python', 'SkeletonV2/page2.py'])
    root.destroy()
        
def on_cancel():
    root.destroy()

button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="Continue", width=10, command=on_ok).grid(row=7, column=0, padx=5)
tk.Button(button_frame, text="Close", width=10, command=on_cancel).grid(row=7, column=1, padx=5)

    # Infinite loop can be terminated by
    # keyboard or mouse interrupt
    # or by any predefined function (destroy())
   
root.mainloop()