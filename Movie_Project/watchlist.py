from tkinter import *
from tkinter import ttk


def watchlist_startup():
    window = Tk()
    window.title("WatchList")
    window.geometry("750x500")

    label = Label(window, text="Welcome to your watchlist!", font=("Dosis", 25))
    label.grid(row = 0, column = 1, columnspan=4)

    box = Listbox(window, font=("Dosis", 15))

    box.grid(row = 4, column=0, columnspan=1, padx=10, pady=5)

    box.insert("end","movie1", "movie2", "movie3", "movie4", "movie5", "movie6")

    cancel = Button(window, text="Cancel", font=("Dosis", 12), command = window.quit)
    cancel.grid(column=5, row=5)

    window.mainloop()

if __name__ == "__main__":
    watchlist_startup()


