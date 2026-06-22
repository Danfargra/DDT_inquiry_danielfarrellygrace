import tkinter as tk
from tkinter import ttk, messagebox, StringVar
from PIL import Image, ImageTk
root = tk.Tk()

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array
        self.frames = {}  
 
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (home_page, page_1):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(home_page)
 
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def home_page():

    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3)

    #logo
    logo = Image.open('v1_skeleton/images/Advisory_logo.png')
    res = logo.resize((300, 300), Image.Resampling.LANCZOS)

    '''logo = Image.open('v1_skeleton/images/Advisory_logo.png').resize((size[0], size[1]), Image.Resampling.LANCZOS)
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
    tk.Label(root, text="Select Notification Choice:").grid(row=4, column=0, columnspan=2)
    advice = tk.StringVar(value="General")
    advice_list = ["Financial", "Relationship", "Career", "General"]

    advice_frame = tk.Frame(root)
    advice_frame.grid(row=5, column=0, columnspan=2)
    for d in advice_list:
        tk.Radiobutton(advice_frame, text=d, variable=advice, value=d).pack(anchor="w")

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
        page_1()

        



    def on_cancel():
        root.destroy()

    button_frame = tk.Frame(root)
    button_frame.grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(button_frame, text="Continue", width=10, command=on_ok).grid(row=7, column=0, padx=5)
    tk.Button(button_frame, text="Cancel", width=10, command=on_cancel).grid(row=7, column=1, padx=5)

def page_1():
    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3)

    #logo

    logo = Image.open('v1_skeleton/images/Advisory_logo.png')
    res = logo.resize((300, 300), Image.Resampling.LANCZOS)


    '''logo = Image.open('v1_skeleton/images/Advisory_logo.png').resize((size[0], size[1]), Image.Resampling.LANCZOS)
    #LANCZOS allows images to be resized'''

    logo = ImageTk.PhotoImage(res)
    #logo in label
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)

    #welcoming
    welcoming = tk.Label(root, text="Home Page", font="Raleway")
    welcoming.grid(columnspan=3, column=0, row=1)


   
    

    # Infinite loop can be terminated by
    # keyboard or mouse interrupt
    # or by any predefined function (destroy())



    #continu to next page button

    # --- Command buttons ---
    def on_ok():
        home_page()

        



   

    button_frame = tk.Frame(root)
    button_frame.grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(button_frame, text="Home", width=10, command=on_ok).grid(row=7, column=0, padx=5)


home_page()
root.mainloop()