import tkinter as tk
from tkinter.ttk import Label
from tkinter import messagebox
from tkinter import *

root = tk.Tk()
root.geometry("400x200")

label = Label(root, text='0', font=('Times', 24)) # text='0'
label.pack(ipadx=10, ipady=10)

def StartTimer():
    messagebox.showinfo('Message', 'You started the timer!')

    inp = label.get(1.0, "end-1c")

    i = 0 
    while i <= inp:
        print (i)
        i = i + 1
    print ("Good Bye!")

# Button #1
button = Button(root, text = "Start Timer", command = StartTimer)
button.pack(side = "top")

# TextBox Creation
inputtxt = tk.Text(root, height = 3, width = 20)

inputtxt.pack()

# pythonguides.com/python-gui-programming/

# Button #1
#btn = Button(root, text = "Start Timer", bd = "5", command = StartTimer)
#btn.pack(side = "top")

# Button #2
btn2 = Button(root, text="Exit Program", bd = "5", command = root.destroy ) # Exit Program
btn2.pack(side = "bottom")

# Window maximize = False
root.resizable(False, False)

# show a label


root.mainloop()