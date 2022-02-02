import tkinter as tk
from tkinter.ttk import Label
from tkinter import messagebox
from tkinter import *
import sys

root_window = tk.Tk()
root_window.geometry("250x150")
root_window.title("Timer by Jamie Morrissey")
root_window.resizable(False, False)


# Declare variables

second = StringVar()

# setting the default value as 0

second.set("00")

# prog link: http://geeksforgeeks.org/create-countdown-timer-using-python-tkinter/?ref=lbp
# Entry widget

secondEntry = Entry(root_window, width = 3, textvariable=second)
secondEntry.place(x=180, y=20)

# label

label = Label(root_window, text="Enter seconds")
label.place(relx = 1.0, rely = 0.0, anchor = 'ne')


def menu_submit():
    # the input from the user is stored here
    try:

    except ValueError:
        print("Please :input a value that is a int")
        sys.exit()


    while temp >-1:


# Button #1
btn = Button(root_window, text = "Start Timer", command = messagebox.showinfo)
btn.place(x=70, y=120)
btn.grid(row=1, column=0)

# button #2

btn_2 = Button(root_window, text = "Exit Program", command = root_window.quit)
btn_2.place(x=80, y=100)
btn_2.grid(row=2, column=0)


# show a label

root_window.mainloop()