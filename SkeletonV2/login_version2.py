import customtkinter as ctk
import tkinter.messagebox as tkmb
import subprocess
#title of window


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("light")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Advisory - Login")


def login():
    #temporary username and password 
    username = "bob"
    password = "12345"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        subprocess.Popen(['python', 'SkeletonV2\main_version2.py'])
        app.destroy()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password',message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username',message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed",message="Invalid Username and password")



label = ctk.CTkLabel(app, text="This is the main UI page")




label.grid(columnspan=3, ipady=20, sticky="n")



frame = ctk.CTkFrame(master=app)
frame.grid(ipady=20,ipadx=40)

label = ctk.CTkLabel(master=frame,text='Modern Login System UI')
label.grid(columnspan=3, column=2, row=0, ipady=12,ipadx=10)


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
user_entry.grid(columnspan=3, column=2, row=1, ipady=12,ipadx=10)

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_pass.grid(columnspan=3, column=2, row=3, ipady=12,ipadx=10)


button = ctk.CTkButton(master=frame,text='Login',command=login)
button.grid(columnspan=3, column=2, row=4, ipady=12,ipadx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.grid(columnspan=3, column=2, row=5, ipady=12,ipadx=10)


app.mainloop()