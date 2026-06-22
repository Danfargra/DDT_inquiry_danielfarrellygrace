import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("360x640")
root.title("Advisory App")
base_dir = os.path.dirname(os.path.abspath(__file__))

# --- Window icon ---
icon = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "ryan.png")))
root.iconphoto(True, icon)

# --- Avatar images ---
img1 = Image.open(os.path.join(base_dir, "ryan.png"))
photo1 = ImageTk.PhotoImage(img1)
label1 = tk.Label(root, image=photo1)
label1.grid(row=0, column=0, padx=5, pady=5)

img2 = Image.open(os.path.join(base_dir, "ryan.png"))
photo2 = ImageTk.PhotoImage(img2)
label2 = tk.Label(root, image=photo2)
label2.grid(row=0, column=1, padx=5, pady=5)

# --- Title ---
title = tk.Label(root, text="Advisory", font=("Arial", 16, "bold"))
title.grid(row=1, column=0, columnspan=2, pady=10)

# --- Dropdown (Types of advice) ---
tk.Label(root, text="Select Topic of Advice:").grid(row=2, column=0, columnspan=2)
house = tk.StringVar(value="Financial")
house_menu = ttk.Combobox(
    root,
    textvariable=house,
    values=["Financial", "Relationship", "Academic", "General"],
    state="readonly",          # stops users typing their own text
)
house_menu.grid(row=3, column=0, columnspan=2, pady=5)

# --- Radio buttons (Notification) ---
tk.Label(root, text="Select Notification Choice:").grid(row=4, column=0, columnspan=2)
day = tk.StringVar(value="Email")
days = ["Email", "Phone Number (text)", "Applicaiton Notification", "None"]

day_frame = tk.Frame(root)
day_frame.grid(row=5, column=0, columnspan=2)
for d in days:
    tk.Radiobutton(day_frame, text=d, variable=day, value=d).pack(anchor="w")

# --- Checkbox (ts and cs) ---
is_teacher = tk.BooleanVar()
tk.Checkbutton(root, text="Agree to Terms and Conditions",
               variable=is_teacher).grid(row=6, column=0, columnspan=2, pady=8)

# --- Command buttons ---
def on_ok():
    role = "Agreed" if is_teacher.get() else "Disagreed"
    messagebox.showinfo(
        "Selection",
        f"Advice: {house.get()}\nContact: {day.get()}\nT&Cs: {role}"
    )

def on_cancel():
    root.destroy()

button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="OK", width=10, command=on_ok).grid(row=7, column=0, padx=5)
tk.Button(button_frame, text="Cancel", width=10, command=on_cancel).grid(row=7, column=1, padx=5)







#progress bar
'''bar = ttk.Progressbar(root, length=200, mode="determinate", maximum=100)
bar.grid(row=10, column=0, pady=5, columnspan=2)

def step():
    bar["value"] += 10          # advance by 10 each click
    if bar["value"] > 100:
        bar["value"] = 0

tk.Button(root, text="Advance", command=step).grid(row=11, column=0, padx=10, pady=10)'''

root.mainloop()