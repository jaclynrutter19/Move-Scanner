from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def boxtext(new_value):
    display.config(text = moods[new_value])

root = Tk()
root.title("Movie Scanner")
root.geometry("400x400")
root.minsize(1000,800)
root.maxsize(1000,1400)

moods =["Lost", "Relaxed", "Empathetic", "Informed", "Stressed", "Sad", "Happy", "Inspired", "Romantic", "Scared", "Weird", "Doesn't matter"]

Label(root, text="1. I want to see a movie that will make me feel...", font=("Dosis", 20)).grid(column=0, row=0, columnspan= 2)
Label(root, text="Please select from the dropdown below.", font=("Dosis", 10)).grid(column=0, row=1)

variable = StringVar(root)
variable.set(moods[0])

dropdown1 = OptionMenu(root, variable, *moods, command=boxtext).grid(column = 0, row = 2, padx=5, pady=5)

# I will be watching a movie with..

people = ["Friends", "Family", "Myself", "My Partner", "Strangers"]

Label(root, text="2. I will be watching a movie with...", font=("Dosis", 20)).grid(column=0, row=5, columnspan= 2)
Label(root, text="Please select from the dropdown below.", font=("Dosis", 10)).grid(column=0, row=6)

variable = StringVar(root)
variable.set(people[0])

dropdown2 = OptionMenu(root, variable, *people, command=boxtext).grid(column = 0, row = 7, padx=5, pady=5)

# I want to watch something that is...
feelings = ["Classic", "Weird", "International", "I'll watch anything!"]

Label(root, text="3. I want to watch something that is..", font=("Dosis", 20)).grid(column=0, row=10, columnspan= 2)
Label(root, text="Please select from the dropdown below.", font=("Dosis", 10)).grid(column=0, row=11)

variable = StringVar(root)
variable.set(feelings[0])

dropdown3 = OptionMenu(root, variable, *feelings, command=boxtext).grid(column = 0, row = 12, padx=5, pady=5)

# I want to watch something that is rated..
ratings = ["G-General audiences all ages", "PG - Parental guidance suggested", "PG-13 - Parents strongly cautioned", "R - Restricted", "Doesn't matter"]

Label(root, text="4. I want to watch something that is rated..", font=("Dosis", 20)).grid(column=0, row=15, columnspan= 2)
Label(root, text="Please select from the dropdown below.", font=("Dosis", 10)).grid(column=0, row=16)

variable = StringVar(root)
variable.set(ratings[0])

dropdown4 = OptionMenu(root, variable, *ratings, command=boxtext).grid(column = 0, row = 17, padx=5, pady=5)

root.mainloop()
