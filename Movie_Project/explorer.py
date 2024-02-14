from tkinter import *
import tkinter as tk
from watchlist import watchlist_startup

def explorer_startup():

    root = Tk()
    root.title("Explorer Page")
    root.geometry("750x750")
    root.anchor('center')

    label = Label(root, text="What would you like to do today?", font=("Dosis", 25))
    label.grid(row = 1, column = 2, columnspan=4, padx=5, pady=5)

    description = Label(root, text="Please select from the options below.", font=("Dosis", 18))
    description.grid(row = 2, column = 2, columnspan=4, padx=5, pady=5)

    movie_butt = tk.Button(root, text="Explore Movies", width=13, height = 15, font=("Dosis", 22))
    movie_butt.grid(row = 5, column = 2, padx=5, pady=5)
    movie_butt_label=Label(root, text="Take our movie quiz and explore recommended movies.", wraplength= 200, font=("Dosis", 10))
    movie_butt_label.grid(row = 6, column = 2, rowspan=2, padx=5, pady=5)

    watchlist_butt = tk.Button(root, text="Explore Watchlist", width=13, height = 15, wraplength= 200, font=("Dosis", 22), command = watchlist_startup)
    watchlist_butt.grid(row = 5, column = 3, padx=5, pady=5)
    watchlist_label=Label(root, text="Explore previously saved movies.", font=("Dosis", 10))
    watchlist_label.grid(row = 6, column = 3, padx=5, pady=5)

    profile_butt = tk.Button(root, text="Explore Profile", width=13, height = 15, wraplength= 200, font=("Dosis", 22))
    profile_butt.grid(row = 5, column = 4, padx=5, pady=5)
    profile_label=Label(root, text="Create and edit your Movie Scanner profile.", font=("Dosis", 10))
    profile_label.grid(row = 6, column = 4, padx=5, pady=5)

    log_out = tk.Button(root, text = "logout", width = 3, heigh = 2, command = root.destroy)
    log_out.grid(row = 0, column =4, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    explorer_startup()