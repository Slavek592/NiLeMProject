#!/usr/bin/python3
import os
from Definitions import Runner
from tkinter import *


def walker(location):
    comment.configure(text="")
    back_button.configure(command=lambda action=Runner.get_outer_path(location, 2): walker(action))
    for widget in frame.winfo_children():
        widget.destroy()
    directories = [f for f in os.listdir(location) if not os.path.isfile(os.path.join(location, f))]
    i = 0
    for directory in directories:
        Button(frame, text=directory + "/",
               command=lambda action=location + directory + "/": walker(action)).grid(row=i, column=0)
        i += 1
    files = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
    i = 0
    for file in files:
        Button(frame, text=file,
               command=lambda action=location + file: interactive_run(action)).grid(row=i, column=1)
        i += 1
    comment.configure(text="Entered into")


def interactive_run(file_name):
    comment.configure(text="")
    if Runner.run_from_file(file_name):
        comment.configure(text="Done")
    else:
        comment.configure(text="Error")


def turn_off():
    print("Thank You for using NiLeSh and NiLeM!")
    print("Goodbye!")
    root.destroy()


print("Welcome, User!")
print("Graphical version of NiLeSh 'compiler' greets You!")
root = Tk()
root.title("NiLeSh")
back_button = Button(root, text="../", command=None)
back_button.pack()
frame = Frame(root)
frame.pack()
turn_off_button = Button(root, text="Turn off", command=turn_off)
turn_off_button.pack()
comment = Label(root, text="")
comment.pack()
walker("NileshScripts/")
comment.configure(text="Welcome, user!")
root.mainloop()
