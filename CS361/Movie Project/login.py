from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from explorer import *

root = Tk()
root.title("Login")

def log_off():
    root.quit()
    explorer_startup()

def val_login():
    username = name_var.get()
    password = pass_var.get()
   
    if username == "rutterj" and password =="testing":
        messagebox.showinfo(message = "Login Succesful", title = "Login Succesful", command = log_off())
    elif username == "" and password == "":
        err_message1 = messagebox.showerror(message = "Please fill out fields.", title = "Failed Login")
        err_message1.destroy()
    else:
        err_message = messagebox.showerror(message = "Login failed, please try again.", title = "Failed Login")
        err_message.destroy()
        

name_var=StringVar()
pass_var=StringVar()

# CREATE login window
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Please enter your credentials below.").grid(column=1, row=0)

ttk.Label(frm, text="Username:").grid(column=0, row=1)
username = Entry(frm, textvariable = name_var).grid(column =1, row=1)

ttk.Label(frm, text="Password:").grid(column=0, row=3)
password = Entry(frm, textvariable = pass_var, show="*").grid(column =1, row=3)

ttk.Button(frm, text="Submit", command=val_login).grid(column=2, row=3)
root.mainloop()