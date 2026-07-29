import tkinter as tk

master = tk.Tk()
master.title = ("Advisory")
menu = tk.Menu(master)
master.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
menu.add_command(label="Exit", command=master.quit)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

master.mainloop()

