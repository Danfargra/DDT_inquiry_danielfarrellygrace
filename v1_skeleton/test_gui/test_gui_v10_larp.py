# Python program to create a basic GUI 

import tkinter as ttk
from tkinter import Tk   
 

appWidth, appHeight = 600, 700

# App Class
class App(ttk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")

        # Name Label
        self.nameLabel = ttk.Label(self,
                                      text="Name")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")



        # Age Label
        self.ageLabel = ttk.Label(self,
                                     text="Age")
        self.ageLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")



        # Gender Label
        self.genderLabel = ttk.Label(self, 
                                    text="Gender")
        self.genderLabel.grid(row=2, column=0, 
                              padx=20, pady=20,
                              sticky="ew")

        

        # Choice Label
        self.choiceLabel = ttk.Label(self,
                                        text="Choice")
        self.choiceLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")


        # Occupation Label
        self.occupationLabel = ttk.Label(self,
                                            text="Occupation")
        self.occupationLabel.grid(row=4, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")

       

        # Generate Button
        self.generateResultsButton = ttk.Button(self,
                                         text="Generate Results")
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")

      
if __name__ == "__main__":
    app = App()
    app.mainloop()