import tkinter as tk

root = tk.Tk()

tk.Label(root, text="First Name").pack()
tk.Label(root, text="Last Name").pack()

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.pack()
entry2.pack()

root.mainloop()

