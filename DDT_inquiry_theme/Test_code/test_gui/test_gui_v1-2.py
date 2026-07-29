# Import Module
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


# create root window
root = tk.Tk()



# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('350x200')

#adding a label to the root window
lbl = Label(root,text = "Are you a Geek?")
lbl.pack()

#function to display text when
#button is clicked
def clicked():
    lbl.configure(text = "I just got clicked")

# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
btn.pack()

# Widgets are added here
WINDOW_WIDTH = 800
HEADER_COLOUR = '#ffffff'
header = tk.Frame(root)
header.pack()

img = Image.open("v1_skeleton\test_gui\Advisory_logo.png").resize((WINDOW_WIDTH, 500))
_ryan_img = ImageTk.PhotoImage(img)
label = tk.Label(header, image=_ryan_img, bg=HEADER_COLOUR)
label.image = _ryan_img  # keep reference
label.pack()
root.mainloop()

# Execute Tkinter
root.mainloop()

#ctrl + shit + p ==> abyss