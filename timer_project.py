import tkinter as tk
from tkinter.ttk import Label
from tkinter import messagebox
from tkinter import *
import time

root_window = tk.Tk()
root_window.geometry("200x200")
root_window.title("Timer by Jamie Morrissey")

label = Label(root_window, text='0', font=('Times', 24)) # text='0'

# Entry widget

e = tk.Entry(root_window)
e.pack(padx=20, pady=20)
e.delete(0, "end")
e.insert(0, "Insert seconds...")

# Button #1
button = Button(root_window, text = "Start Timer", command = root_window.destroy)
button.pack(side = "top")

# Button #2
btn2 = Button(root_window, text="Exit Program", bd = "5", command = root_window.destroy ) # Exit Program
btn2.pack(side = "bottom")

# Window maximize = False
root_window.resizable(False, False)

# show a label


root_window.mainloop()
